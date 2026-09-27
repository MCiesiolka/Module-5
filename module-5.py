# Broken Access Control
# 1
app.get("profile/:userID", ensureAuthenticated, (req, res) => {
    if (req.status.id !== req.params.userId && !req.user.isAdmin) {
        return res.status(403).send("Access Denied");
    }

    User.findById(req.params.userId, (err, user) => {
        if (err) return res.status(500).send(err);
        res.json(user);
    });
});

# 2
@app.route("/account")
@login_required
def get_account():
    user_id = session.get("user_id")
    user = db.query(User).filter_by(id=user_id).first()
    return jsonify(user.to_dict())

# Cryptographic Failures
# 3
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;

public String hashPassword(String password) {
    BCryptPasswordEncoder encoder = new BCryptPasswordEncoder(12);
    return encoder.encode(password);
}

# 4
import bcrypt 

def hash_password(password: str) -> str:
    salt = bcrypt.gensalt(rounds=12)
    hashed = bcrypt.hashpw(password.encode(), salt)
    return hashed.decode()

# Injection
# 5
String username = request.getParameter("username");
String query = "SELECT * FROM users WHERE username = ?" 
PreparedStatement stmt = connection.prepareStatement(query);
stmt.setString(1, username);
ResultSet rs = stmt.executeQuery();

# 6
app.get("/user", (req, res) => {
    const usernameParam = String(req.query.username);

    db.collection("users").findOne({ username: usernameParam }, (err, user) => {
        if (err) return res.status(500).json({ error: err.message });
        res.json(user);
    });
});

# Insecure Design
# 7
@app.route("/forgot-password", methods=["POST"])
def forgot_password():
    email = request.format["email"]
    user = User.query.filter_by(email=email).first()
    if user:
        token = generate_secure_token()
        save_token_to_db(user.id, token)
        send_reset_email(user.email, token)
    return "If the email matches, a reset link was sent."

# SOftware and Data Integrity Failures
# 8
< script
    src="https://cdn.example.com/lib.js"
    integrity="sha384-oqVuAfXRKap7fdgcCY5uykM6+R9GqQ8K/uxy9rx7HNQlGYl1kPzQho1wx4JwY8mC"
    crossorigin="anonymous" >
</script>

# Server-Side Request Forgery
# 9
from urllib.parse import urlparse
import requests

ALLOWED_DOMAINS = ["://trustedservice.com ", "://api.trustedservice.com"]

def safe_fetch(user_url):
    parsed_url = urlparse(user_url)
    if parsed_url.netloc not in ALLOWED_DOMAINS:
        raise ValueError("Target domain is unauthorized.")

    if parsed_url.scheme not in ["http", "https"]:
        raise ValueError("Invalid URL scheme.")

    response = requests.get(user_url, timeout=5)
    return response.text

# Identification and Authentication Failures
# 10
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;

BCryptPasswordEncoder encoder = new BCryptPasswordEncoder();

if (encoder.matches(inputPassword, user.getPasswordHash())) {

}