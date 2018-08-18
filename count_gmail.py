#!/usr/bin/env python

import mailbox
import rfc822
import email
import time
import sys
import os.path

md_name = os.path.expanduser(sys.argv[1])

inbox = mailbox.Maildir(md_name, factory=None)

def cls_mail(mail_str):
  if mail_str == None:
    mail_str = "NA"
  else:
    mail_str = email.utils.parseaddr(mail_str)[1]
  return mail_str


for intermsg in inbox.items():
    #flags = msg.get_flags()
    #date = msg.get_date()
    msg = intermsg[1]
    date = msg.get("Date")

    if date == None:
        continue
    else:
        date = email.utils.parsedate(date)
        if date == None:
            continue
        else:
            date = time.mktime(date)


    #delivered = cls_mail(msg.get("Delivered-To"))
    #sender = cls_mail(msg.get("Sender"))
    sender= cls_mail(msg.get("From"))
    to = cls_mail(msg.get("To"))

    if len(sender.split("@")) >= 1:
      sender_domain = '.'.join(sender.split("@")[1].split(".")[-2:])
    else:
      sender_domain = "NA"

    if len(to.split("@")) >= 1:
      to_domain = '.'.join(to.split("@")[1].split(".")[-2:])
    else:
      to_domain = "NA"

    if intermsg[0].split(",") >= 1:
      msg_size = intermsg[0].split(",")[1].split("=")[1]
    else:
      msg_size = "NA"

    # put it together and output
    print("\t".join([str(date), to, sender, sender_domain, msg_size]))
