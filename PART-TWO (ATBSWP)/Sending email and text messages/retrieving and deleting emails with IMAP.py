import imapclient, pprint, imaplib, pyzmail

imapObj = imapclient.IMAPClient('imap.gmail.com', ssl=True)
imapObj.login('boluwatifelekeoduoye@gmail.com', '**********')
"b'boluwatifelekeoduoye@gmail.com authenticated (Success)'"
pprint.pprint(imapObj.list_folders())
'''[((b'\\HasNoChildren',), b'/', 'Drafts'),
 ((b'\\HasNoChildren',), b'/', 'INBOX'),
 ((b'\\HasChildren', b'\\Noselect'), b'/', '[Gmail]'),
 ((b'\\All', b'\\HasNoChildren'), b'/', '[Gmail]/All Mail'),
 ((b'\\Drafts', b'\\HasNoChildren'), b'/', '[Gmail]/Drafts'),
 ((b'\\HasNoChildren', b'\\Important'), b'/', '[Gmail]/Important'),
 ((b'\\HasNoChildren', b'\\Sent'), b'/', '[Gmail]/Sent Mail'),
 ((b'\\HasNoChildren', b'\\Junk'), b'/', '[Gmail]/Spam'),
 ((b'\\Flagged', b'\\HasNoChildren'), b'/', '[Gmail]/Starred'),
 ((b'\\HasNoChildren', b'\\Trash'), b'/', '[Gmail]/Trash')]'''
imapObj.select_folder('INBOX', readonly=True)
'''{b'PERMANENTFLAGS': (), b'FLAGS': (b'\\Answered', b'\\Flagged',...'''
UIDs = imapObj.search(['SINCE', '05-Jul-2022'])
UIDs
'''[3454, 3455, 3456, 3457, 3458, 3459, 3460, 3461, 3462, 3463, 3464, 3465,
3466, 3467, 3468, 3469, 3470, 3471, 3472, 3473, 3474, 3475, 3476, 3477,
3478, 3479, 3480, 3481, 3482, 3483, 3484, 3485, 3486, 3487, 3488, 3489,...]'''

imaplib.MAXLINE = 10000000
UIDs = imapObj.gmail_search('babs')
UIDs
"[3405, 3429]"
rawMessages = imapObj.fetch(UIDs, ['BODY[]'])
pprint.pprint(rawMessages)
'''defaultdict(<class 'dict'>,
            {3405: {b'BODY[]': b'Delivered-To: boluwatifelekeoduoye@gmail.com'
                               b'\r\nReceived: by 2002:a9a:7e97:0:b0:1f4:eff0:6'
                               b'f4 with SMTP id l23csp66713lkh;\r\n        Wed'
                               b', 29 Jun 2022 01:16:15 -0700 (PDT)\r\nX-Google'...'''

message = pyzmail.PyzMessage.factory(rawMessages[3405][b'BODY[]'])
message.get_subject()
'GeNS Transaction Alert [Debit: NGN 1,000.00]'
message.get_address('from')
"('GeNS@gtbank.com', 'GeNS@gtbank.com')"
message.get_address('to')
"('boluwatifelekeoduoye@gmail.com', 'boluwatifelekeoduoye@gmail.com')"
message.get_address('cc')
"('', '')"
message.get_address('bcc')
"('', '')"
message.text_part != None
'False'
message.html_part != None
'True'
message.html_part.get_payload().decode(message.html_part.charset)
'''<HTML>\r\n<BODY>\r\n<style type="text/css">\r\n h4 {\r\n
font-family: Calibri, Tahoma, Geneva, sans-serif;\r\n    }\r\n    table {\r\n...'''

imapObj = imapclient.IMAPClient('imap.gmail.com', ssl=True)
imapObj.login('boluwatifelekeoduoye@gmail.com', '*********')
b'boluwatifelekeoduoye@gmail.com authenticated (Success)'
imapObj.select_folder('INBOX', readonly=False)
'''{b'PERMANENTFLAGS': (b'\\Answered', b'\\Flagged', b'\\Draft', b'\\Deleted', b'\\Seen'...)}'''
UIDs = imapObj.search(['ON', '09-Feb-2022'])
UIDs
"[2352, 2353, 2354, 2355, 2356, 2357, 2358, 2359, 2360, 2361]"
imapObj.delete_messages(UIDs)
'''{2352: (b'\\Deleted',), 2353: (b'\\Deleted',), 2354: (b'\\Deleted',),...'''
imapObj.expunge()
(b'Success', [])
imapObj.logout()
"b'LOGOUT Requested'"