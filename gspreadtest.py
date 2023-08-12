import gspread

credentials = {
  "type": "service_account",
  "project_id": "data-sort-test-392421",
  "private_key_id": "4012bed2ee80d67a111f5bb67b16c65946d1dcb0",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDG+8cI/OPEiafJ\n7e2tjx8vf65F7bl+udlwgdnvy6445uRiNXOquQ/h2qsfTBblY6EXHn+u9v8PD4v8\n/ICu/OMf86zI3gShIyQVzpuxt9dGrZpbWb2I5F4rxkfHxYJFSXOBpnFQvzBGidMg\nUfkhq+Zbcda4iCkoZjaUop/oOZSpTH8vGSuPjung0QIkQgJi7T3REl+Rdl5XgUFZ\nJMqwM7vjEO7fsumEdowlfiQuhE6hQ7MjDSYohiF3jBKt+1YM0lQGf/tu4+7Ztp6N\n1zEQb/9edqoDFvAXCaQlq6hB9Nrm5kXLRppLyyP+NzbptOzPSjD4Kq+mzalGOoqm\nGHVbp0a/AgMBAAECggEAKU3yTudP0GhSsBP3lmNzMcTrRBDIxImHnVcXCjPZgm5L\nUieOTw4DQfrGMsT0q8E2mzn1fzg+Ub4EbQttGuXbr7JBV6DejSRiRTSSFR34Te+T\nbwr90QC2m5eZJtrU49UPaQZH118Ygkvxy2+4q0inlKvYyo1ZHc253rizQN1TAqFE\ntmlZqgCYuSi3tBRqM6riRPDN2sXjy6KI4+3FZwKLiF5krMY5U/JeB1Ssoz0jUqsj\ngm+qiJBTItXlnZIrmrFSySbFelfMc6GvsLZpXCNDIfBlMgnWlpqWYKoArgdVl5pG\npm/qx29qr2BkRIsQzZ3YKe69ITP4F7Ly0Ts8f3hZwQKBgQDox3oJOnbGrfoWaaEP\npxZTnznwFruBTP2bZ0KnkDjfz/aD8K0i3ybTGactFb32RM2tdFybycsErUYT6fyt\ndEX7Eh6aKHgz/ypvFbR3ZesZ3q8XlwPGVX16e4Il0gjZeqIMKjpLaCG/yEZE7i9i\no361icymTPQ/2waGV0xOQh2fqQKBgQDa1UEK71v7RXrY0hyAeCZKUgEHnK6yQgVo\nQDD/R+AD1rLmK2lSPAL7x9F4kPNihsr2mS1mAmTH+XMTGVtyYkJ6VCwc+4BNRLdU\nO21H4dUTKqfmFCzk8vqkv5uFco5f1X/MUh1fPEpu/0+k4uuVTGm+4Qb26RI3vtkx\nBBbKPQzUJwKBgQC2ekE5YMJhp1qoHS/sJFCFRwnVIwzkJKWeIEmJL67WDKGz9oTT\nFFnMHI0H88ZResg9VD2QxpTG2spXrBKvKrn9QswIjvcD0+DA6iPpgVTWl9FsTa7g\n2H2f+Zgh68+SJOdJYAUIvd3PCMHFIW62BXK7/wUVzLegIyOvRloD8yJj2QKBgC6b\nWL0Bea+sfpuLNHLQJCeUC5AZeMOSeCBZ+5WDM1zd70BCYq4XBfOl/SEWjh+f4b5f\npWGihOBqam3Y6rcT4mC3aKXLkuniBsGz3nR+zqjEXvoLtfwVG/jWrkLfwR78E7nq\ni0LrTlcRnV7azZ4Apkz3FEqmHTEuPofH/SqZkg/lAoGACJt43VhAXM8en1YAXJqg\nRpx9w+lteuIwJwDgOb5e/MDJHxQA6BdIS5w6d7UY/4g2K6xb9t7Ty1JsVVz2wy26\n0OrXgIRVkRRAnSCGwCGzH8DyGOj96VVb75jMZYlOeOYYzNeTswCp0Vc7KLNDWOqB\nfCsJ4Zyf/48bme7Czc8ter8=\n-----END PRIVATE KEY-----\n",
  "client_email": "duckycodetesting@data-sort-test-392421.iam.gserviceaccount.com",
  "client_id": "110295960811356694841",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/duckycodetesting%40data-sort-test-392421.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"
}

gc = gspread.service_account_from_dict(credentials)

sh = gc.open_by_url("https://docs.google.com/spreadsheets/d/1AFVfTbSo2PIV6F1DmxTk1I-fzJW7CgHj98-E7vmclnw/edit?usp=sharing")

print(sh.sheet1.get('A1'))

