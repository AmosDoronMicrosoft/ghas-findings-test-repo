#!/usr/bin/env python3
"""
Configuration file with hardcoded secrets
SECURITY VULNERABILITIES FOR TESTING - GitHub Secret Scanning
"""

# Database credentials
DATABASE_CONFIG = {
    'host': 'postgres.production.example.com',
    'port': 5432,
    'username': 'postgres_admin',
    'password': 'PostgresP@ssw0rd2024!',
    'database': 'production_db',
    'connection_string': 'postgresql://dbuser:MySecretPass123@db.example.com:5432/appdb'
}

# AWS Credentials
AWS_ACCESS_KEY_ID = 'AKIAIOSFODNN7EXAMPLE'
AWS_SECRET_ACCESS_KEY = 'wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY'
AWS_SESSION_TOKEN = 'FwoGZXIvYXdzEBQaDEXAMPLETOKEN1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
AWS_REGION = 'us-west-2'

# Azure credentials
AZURE_STORAGE_CONNECTION_STRING = 'DefaultEndpointsProtocol=https;AccountName=mystorageaccount;AccountKey=abcd1234EFGH5678ijkl9012MNOP3456qrst7890uvwx1234yzAB5678CDEF9012==;EndpointSuffix=core.windows.net'
AZURE_CLIENT_ID = '12345678-1234-1234-1234-123456789012'
AZURE_CLIENT_SECRET = 'abcdefghijklmnopqrstuvwxyz1234567890ABCD'
AZURE_TENANT_ID = '87654321-4321-4321-4321-210987654321'

# Google Cloud Platform
GCP_API_KEY = 'AIzaSyDaGmWKa4JsXZ-HjGw47623Hb5YP0Sk1p9'
GCP_SERVICE_ACCOUNT_KEY = '''{
  "type": "service_account",
  "project_id": "my-project-123456",
  "private_key_id": "1234567890abcdef1234567890abcdef12345678",
  "private_key": "-----BEGIN PRIVATE KEY-----\\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQC1234567890abc\\ndefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ\\n-----END PRIVATE KEY-----\\n",
  "client_email": "service-account@my-project-123456.iam.gserviceaccount.com",
  "client_id": "123456789012345678901",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token"
}'''

# API Keys and Tokens
STRIPE_SECRET_KEY = 'sk_live_51HqXYZ1234567890abcdefghijklmnopqrstuvwxyz'
STRIPE_PUBLISHABLE_KEY = 'pk_live_51HqXYZ9876543210zyxwvutsrqponmlkjihgfedcba'
GITHUB_TOKEN = 'ghp_1234567890abcdefghijklmnopqrstuvwxyz'
GITHUB_PERSONAL_ACCESS_TOKEN = 'github_pat_11AABBCCDD1234567890_ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890ABCDEFGHIJKLMNOPQR'
SLACK_BOT_TOKEN = 'xoxb-1234567890123-1234567890123-AbCdEfGhIjKlMnOpQrStUvWx'
SLACK_WEBHOOK_URL = 'https://hooks.slack.com/services/T00000000/B00000000/XXXXXXXXXXXXXXXXXXXX'
SENDGRID_API_KEY = 'SG.1234567890abcdefghijklm.nopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ'
TWILIO_ACCOUNT_SID = 'AC1234567890abcdef1234567890abcdef'
TWILIO_AUTH_TOKEN = '1234567890abcdef1234567890abcdef'
OPENAI_API_KEY = 'sk-proj-1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
FIREBASE_API_KEY = 'AIzaSyBBBBCCCCDDDDEEEEFFFFGGGGHHHHIIII'
FIREBASE_AUTH_DOMAIN = 'my-app.firebaseapp.com'

# JWT Secrets
JWT_SECRET_KEY = 'super-secret-jwt-key-for-token-signing-2024'
JWT_REFRESH_SECRET = 'refresh-token-secret-key-that-is-very-long-and-secure'

# OAuth Credentials
OAUTH_CLIENT_ID = 'my-oauth-client-id-12345678'
OAUTH_CLIENT_SECRET = 'my-oauth-client-secret-abcdefghijklmnop'
GOOGLE_OAUTH_CLIENT_ID = '123456789012-abcdefghijklmnopqrstuvwxyz123456.apps.googleusercontent.com'
GOOGLE_OAUTH_CLIENT_SECRET = 'GOCSPX-1234567890abcdefghijklmnop'

# Database URLs
MONGODB_URI = 'mongodb+srv://admin:MongoSecretPass123@cluster0.mongodb.net/mydb?retryWrites=true&w=majority'
REDIS_URL = 'redis://:RedisPassword123@redis.example.com:6379/0'
ELASTICSEARCH_URL = 'https://elastic:ElasticSecurePass@elasticsearch.example.com:9200'

# Payment Gateway Credentials
PAYPAL_CLIENT_ID = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz123456789012'
PAYPAL_CLIENT_SECRET = 'EEEEddddCCCCbbbbAAAA1111222233334444555566667777888899990000'
SQUARE_ACCESS_TOKEN = 'EAAAEOa1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s9t0u1v2w3x4y5z6A7B8C9'

# Email Configuration
SMTP_USERNAME = 'notifications@company.com'
SMTP_PASSWORD = 'EmailSmtpPassword123!'
SENDGRID_USERNAME = 'apikey'
SENDGRID_PASSWORD = 'SG.abcdefghijklmnopqrstuvwxyz.1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# Social Media API Credentials
TWITTER_API_KEY = 'twitter_api_key_abcdefghijklmnopqrstuv'
TWITTER_API_SECRET = 'twitter_api_secret_wxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ'
TWITTER_ACCESS_TOKEN = '1234567890-abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOP'
TWITTER_ACCESS_SECRET = 'twitter_access_secret_QRSTUVWXYZ1234567890abcdefghijk'
FACEBOOK_APP_ID = '1234567890123456'
FACEBOOK_APP_SECRET = 'abcdef1234567890ghijklmnopqrstuv'

# Encryption Keys
ENCRYPTION_KEY = 'a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s9t0u1v2w3x4'
AES_KEY = 'this-is-a-32-byte-aes-key-12345'
RSA_PRIVATE_KEY = '''-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEA1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMN
OPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQR
STUVWXYZabcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUV
WXYZabcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ
-----END RSA PRIVATE KEY-----'''

# Admin Credentials
ADMIN_USERNAME = 'root'
ADMIN_PASSWORD = 'RootAdmin123!@#'
SUPERUSER_PASSWORD = 'SuperUser@Password2024'
DEFAULT_PASSWORD = 'Password123!'
SOME_CHANGE1 = "oihoihff;ln;lnkl"

# API Endpoints with credentials
API_ENDPOINT = 'https://api.example.com/v1'
API_KEY = 'api_key_1234567890abcdefghijklmnopqrstuvwxyz'
API_SECRET = 'api_secret_zyxwvutsrqponmlkjihgfedcba0987654321'
WEBHOOK_SECRET = 'whsec_1234567890abcdefghijklmnopqrstuvwxyz'

# Third-party Service Tokens
DATADOG_API_KEY = 'abcdef1234567890ghijklmnopqrstuv123456'
NEW_RELIC_LICENSE_KEY = '1234567890abcdefghijklmnopqrstuvwxyz1234'
SENTRY_DSN = 'https://abcdef1234567890@o123456.ingest.sentry.io/1234567'

# Shopify credentials
SHOPIFY_API_KEY = 'shpat_abcdef1234567890ghijklmnopqrstuv'
SHOPIFY_API_SECRET = 'shpss_1234567890abcdefghijklmnopqrstuvwxyz'

# Docker credentials
DOCKER_USERNAME = 'dockeruser'
DOCKER_PASSWORD = 'DockerPassword123!'
DOCKER_REGISTRY_TOKEN = 'dckr_pat_1234567890abcdefghijklmnopqrstuvwxyz'

# Private SSH key
SSH_PRIVATE_KEY = '''-----BEGIN OPENSSH PRIVATE KEY-----
b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAABFwAAAAdzc2gtcn
NhAAAAAwEAAQAAAQEA1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOP
-----END OPENSSH PRIVATE KEY-----'''

# SSL Certificate Private Key
SSL_PRIVATE_KEY = '''-----BEGIN PRIVATE KEY-----
MIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQC1234567890abcd
efghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789
-----END PRIVATE KEY-----'''