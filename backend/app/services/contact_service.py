import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from uuid import uuid4

from app.core.config import settings
from app.core.logging import get_logger
from app.repositories.base import BaseRepository
from app.schemas.contact import ContactRequest, ContactResponse

logger = get_logger(__name__)

_HTML_TEMPLATE = """\
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <style>
    body  {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; background:#0a0a0b; color:#e4e4e7; margin:0; padding:0; }}
    .wrap {{ max-width:560px; margin:40px auto; background:#111113; border:1px solid rgba(255,255,255,0.08); border-radius:12px; overflow:hidden; }}
    .hdr  {{ background:#3b82f6; padding:24px 32px; }}
    .hdr h1 {{ margin:0; font-size:1.1rem; font-weight:600; color:#fff; letter-spacing:-0.02em; }}
    .hdr p  {{ margin:4px 0 0; font-size:0.8rem; color:rgba(255,255,255,0.75); }}
    .body {{ padding:28px 32px; }}
    .row  {{ margin-bottom:18px; }}
    .lbl  {{ font-size:0.7rem; text-transform:uppercase; letter-spacing:0.08em; color:#52525b; margin-bottom:4px; }}
    .val  {{ font-size:0.9rem; color:#f4f4f5; }}
    .msg-box {{ background:#18181b; border:1px solid rgba(255,255,255,0.07); border-radius:8px; padding:16px; margin-top:4px; font-size:0.875rem; color:#a1a1aa; line-height:1.6; white-space:pre-wrap; }}
    .footer {{ padding:16px 32px; border-top:1px solid rgba(255,255,255,0.07); font-size:0.75rem; color:#52525b; }}
  </style>
</head>
<body>
  <div class="wrap">
    <div class="hdr">
      <h1>📬 New message — HD Tech Portfolio</h1>
      <p>Someone reached out through your contact form</p>
    </div>
    <div class="body">
      <div class="row">
        <div class="lbl">Name</div>
        <div class="val">{name}</div>
      </div>
      <div class="row">
        <div class="lbl">Email</div>
        <div class="val"><a href="mailto:{email}" style="color:#60a5fa;text-decoration:none;">{email}</a></div>
      </div>
      {need_block}
      <div class="row">
        <div class="lbl">Message</div>
        <div class="msg-box">{message}</div>
      </div>
    </div>
    <div class="footer">HD Tech Portfolio · Curitiba, Brazil</div>
  </div>
</body>
</html>
"""

_NEED_BLOCK = """\
      <div class="row">
        <div class="lbl">What they need</div>
        <div class="val">{need}</div>
      </div>
"""


def _send_email(data: ContactRequest) -> None:
    if not settings.SMTP_USER or not settings.SMTP_PASSWORD:
        logger.warning("SMTP not configured — skipping email send")
        return

    need_block = _NEED_BLOCK.format(need=data.need) if data.need else ""
    html_body = _HTML_TEMPLATE.format(
        name=data.name,
        email=data.email,
        need_block=need_block,
        message=data.message,
    )
    plain_body = (
        f"Name: {data.name}\n"
        f"Email: {data.email}\n"
        + (f"Need: {data.need}\n" if data.need else "")
        + f"\nMessage:\n{data.message}"
    )

    msg = MIMEMultipart("alternative")
    msg["Subject"] = f"[HD Tech] New message from {data.name}"
    msg["From"] = f"HD Tech Portfolio <{settings.SMTP_USER}>"
    msg["To"] = settings.CONTACT_EMAIL
    msg["Reply-To"] = data.email
    msg.attach(MIMEText(plain_body, "plain"))
    msg.attach(MIMEText(html_body, "html"))

    with smtplib.SMTP(settings.SMTP_HOST, settings.SMTP_PORT, timeout=10) as server:
        server.ehlo()
        server.starttls()
        server.login(settings.SMTP_USER, settings.SMTP_PASSWORD)
        server.sendmail(settings.SMTP_USER, settings.CONTACT_EMAIL, msg.as_string())

    logger.info("Email sent to %s for contact from %s", settings.CONTACT_EMAIL, data.email)


def handle_contact(
    data: ContactRequest,
    repo: BaseRepository[ContactResponse],
) -> ContactResponse:
    entry = ContactResponse(
        id=uuid4(),
        name=data.name,
        email=data.email,
        need=data.need or "",
        message=data.message,
        status="received",
    )
    repo.save(entry)
    logger.info("Contact received | id=%s email=%s", entry.id, entry.email)

    try:
        _send_email(data)
    except Exception as exc:
        logger.error("Failed to send contact email: %s", exc)

    return entry


def list_contacts(repo: BaseRepository[ContactResponse]) -> list[ContactResponse]:
    return repo.list_all()
