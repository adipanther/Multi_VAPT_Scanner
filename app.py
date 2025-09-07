from flask import Flask, render_template, request, jsonify
from services.url_analysis import url_analysis
from services.headers import check_headers
from services.subdomain import subdomain_enum
from services.sql_injection import sql_injection_test
from services.xss import xss_test
from services.redirect import redirect_check
from services.restricted_access import restricted_access_check
from services.credential_tester import credential_test

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/scan/url", methods=["POST"])
def scan_url():
    target = request.json.get("target")
    return jsonify(url_analysis(target))

@app.route("/scan/headers", methods=["POST"])
def scan_headers():
    target = request.json.get("target")
    return jsonify(check_headers(target))

@app.route("/scan/subdomain", methods=["POST"])
def scan_subdomain():
    target = request.json.get("target")
    return jsonify(subdomain_enum(target))

@app.route("/scan/sql", methods=["POST"])
def scan_sql():
    target = request.json.get("target")
    return jsonify(sql_injection_test(target))

@app.route("/scan/xss", methods=["POST"])
def scan_xss():
    target = request.json.get("target")
    return jsonify(xss_test(target))

@app.route("/scan/redirect", methods=["POST"])
def scan_redirect():
    target = request.json.get("target")
    return jsonify(redirect_check(target))

@app.route("/scan/restricted", methods=["POST"])
def scan_restricted():
    target = request.json.get("target")
    return jsonify(restricted_access_check(target))

@app.route("/scan/credentials", methods=["POST"])
def scan_credentials():
    data = request.json
    return jsonify(credential_test(data.get("target"), data.get("username"), data.get("password")))

if __name__ == "__main__":
    app.run(debug=True)
