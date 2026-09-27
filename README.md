# Module-5
# Broken Access Control
# 1
Security Flaw - This code is an example of Insecure Direct Object Reference. It trusts the user supplied user:id from the URL 
to fetch database record with out verifying who is logged in. Anyone could access any user profile by alternating the ID in the URL.
The Fix - My fix adds (ensureAuthenticated) and checks if the user logged in matches the ID requested. By rejecting unauthorized requests with a 403 status code, this will ensure data visibility is restricted to the rightful owner. 
A01:2021 - Broken Access Control

# 2
Security Flaw - This code also has an IDOR flaw by reading a primary key user_id from a public URL path. The code trusts that the client owns the account specified in the path. the attacker can enumerate integer ID to scrape every user account in the database. 
The Fix - My fix replaces the user-controlled URL parameter with server managed session variables. By querying the database with session.get the application derives identity from a tamper-proof cookie created during login. This removes the ability to manipulate account ownership.
A01:2021 - Broken Access Control

# Cryptographic Failures
# 3
Security Flaw - The code uses MD5, a broken hashing algorithm prone to collision attacks. MD5 also executes too quickly. Modern Hardware can compute billions of MD5 hashes per second allowing brute force to be made easily. The lack of salt also means the hashings are vulnerable to pre-computed table lookups.
The Fix - By using bcrypt it introduces a strong and adaptive hashing algorithm that can utilize an adjustable work factor to slow down computing. This makes Brute Force Attacks very expensive and impractical. Bcrypt automatically embeds a unique and random salt for every password rendering rainbow tables useless. 
A02:2021 - Cryptographic Failures

# 4
Security Flaw - This code relies on SHA-1 to hash passwords. This has mathematical vulnerabilities and is optimized for speed. Attackers who have good GPUs can crack SHA-1 hashes easily.
The Fix - My fix transitions the password mechanism to bcrypt generating a dynamic salt. The system ensures that users share the same password, their hashes will look entirely different, hindering mass offline cracking attempts.
A02:2021 - Cryptographic Failures

# Injection
# 5
Security Flaw - This is an SQL Injection. The application constructs a database query using string concatenation using raw input from request.getParameter("username"). The attacker can input SQL elements to manipulate the logic of SQL statements and bypass authorization or dump database contents. 
The Fix - My fix uses a PreparedStatement with placeholders. This creates a separation between code and data. The database treats the input as a value string, neutralizing any embedded SQL commands. 
A03:2021 - Injection 

# 6 
Security flaw - This code is vulnerable to a NoSQL Injection. It will accept queries as objects or strings. If req.query.username receives an object instead of a string the database could evaluate the condition as true and expose the first user in record.
The Fix - My fix cleans the query parameter by casting to a primitive string using String(req.query.username). If an attacker submits a nested query object, it turned into harmless text string. 
A03:2021 - Injection

# Insecure Design
# 7 
Security Flaw - The code trusts information across an unauthenticated workflow. By Allowing the user to provide email and a new password to overwrite a database record. This allows any attacker to change a users password by knowing their email address. 
The Fix - My fix changes the code into a secure, multi-step out-of-band workflow. It generates a high entropy and short lived cryptographic token, instead of updating the password immediately. Then is stores it safely and sends a unique verification link to the email. 
A04:2021 - Insecure Design 

# Software and Data Integrity Failures
# 8
Security Flaw - This code imports a 3rd party JavaScript file from an external CDN without verifying integrity. If an attacker compromises the CDN and injects code, the app will fetch and execute that payload in the browsers of all visiting users, starting a supply chain attack. 
The Fix - My fix implements Subresource Integrity by adding the integrity hash attribute. The browser computes a cryptographic check of the downloaded script file and compares it to the specified hash. If the CDN file has been modified by a single character, the browser safely blocks the script from running. 
A08:2021 - Software and Data Integrity Failures

# Server-Side Request Forgery 
# 9
Security Flaw - This code forces the server to make web requests to a URL supplied directly by an untrusted user. The attacker can use this to make a server scan internal private networks, extract cloud metadata endpoints, or interact with local loopbacks that are closed to public internet. 
The Fix - My fix applies strict allowist validation using urllib.parse. By forcing incoming URL to match pre-approved lists of trusted domains and enforcing safe application layer protocols, it prevents attackers from exploiting internal endpoints or using alternative handlers. 
A10:2021 - Server-Side Request Forgery

# Identification and Authentication Failures
# 10
Security Flaw - This application preforms a plain text comparison. This will reveal 2 flaws: 1st that passwords are being handled and checked unhashed; 2nd storing passwords this way implies the reside in plain text in the database, which can lead to total credential exposure if the storage layer is compromised.
The Fix - By using BCryptPasswordEncoder.matches(), it ensures the system will only store non-reversible cryptographic hashes in the database. When someone logs in, the helper method computes the validation hash and preforms a consistent-time comparison, which blocks attackers from using side-channel timing attacks to guess passwords. 
A07:2021 Identification and Authentication Failures 
