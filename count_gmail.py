#!/usr/bin/env python

import mailbox
import rfc822
import email
import time
import sys
import os.path
import logging

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
        logging.warning('No Date! Key: %s', intermsg[0])  # will print a message to the console
        continue
    else:
        date = email.utils.parsedate(date)
        if date == None:
            logging.warning('No Date, after utils parsing! Key: %s', intermsg[0])  # will print a message to the console
            continue
        else:
            date = time.mktime(date)


    #delivered = cls_mail(msg.get("Delivered-To"))
    #sender = cls_mail(msg.get("Sender"))
    sender= cls_mail(msg.get("From"))
    to = cls_mail(msg.get("To"))

    try:
      sender_domain = '.'.join(sender.split("@")[1].split(".")[-2:])
    except:
      sender_domain = "NA"
      logging.warning('Split for Sender doomain failed. Key: %s', intermsg[0])  # will print a message to the console

    try:
      to_domain = '.'.join(to.split("@")[1].split(".")[-2:])
    except:
      to_domain = "NA"
      logging.warning('Split for To doomain failed. Key: %s', intermsg[0])  # will print a message to the console

    try:
      msg_size = intermsg[0].split(",")[1].split("=")[1]
    except:
      msg_size = "NA"
      logging.warning('Split for message size failed. Key: %s', intermsg[0])  # will print a message to the console


    # put it together and output
    print("\t".join([str(date), to, sender, to_domain, sender_domain, msg_size]))
