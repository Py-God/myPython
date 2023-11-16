import smtplib

smtpObj = smtplib.SMTP_SSL('smtp.gmail.com', 465)
smtpObj.ehlo()
(250, b'smtp.gmail.com at your service, [102.89.46.106]\nSIZE 35882577\n8BITMIME\nAUTH LOGIN PLAIN XOAUTH2 PLAIN-CLIENTTOKEN OAUTHBEARER XOAUTH\nENHANCEDSTATUSCODES\nPIPELINING\nCHUNKING\nSMTPUTF8')
smtpObj.login('boluwatifelekeoduoye@gmail.com', '*********')
(235, b'2.7.0 Accepted')
smtpObj.sendmail('boluwatifelekeoduoye@gmail.com', 'lekeoduoyee@gmail.com', 'Subject: So long.\nDear Babs, so long and thanks for all the fish. Sincerely, Bolu')
{}
smtpObj.quit()
