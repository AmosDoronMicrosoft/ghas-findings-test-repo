// Configuration file with hardcoded secrets
// SECURITY VULNERABILITIES FOR TESTING

module.exports = {
  // Database credentials
  database: {
    host: 'db.production.example.com',
    port: 5432,
    username: 'dbadmin',
    password: 'DbP@ssw0rd2024!',
    connectionString: 'postgresql://admin:SecurePass123@db.example.com:5432/maindb'
  },

  // AWS Credentials
  aws: {
    accessKeyId: 'AKIAIOSFODNN7EXAMPLE',
    secretAccessKey: 'wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY',
    region: 'us-east-1',
    s3Bucket: 'my-secure-bucket'
  },

  // API Keys and Tokens
  apiKeys: {
    stripe: 'sk_live_51HqXYZ1234567890abcdefghijklmnopqrstuvwxyz',
    stripePublic: 'pk_live_51HqXYZ9876543210zyxwvutsrqponmlkjihgfedcba',
    github: 'ghp_1234567890abcdefghijklmnopqrstuvwxyz',
    githubToken: 'github_pat_11AABBCCDD1234567890_ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890ABCDEFGHIJKLMNOPQR',
    slack: 'xoxb-1234567890-1234567890123-AbCdEfGhIjKlMnOpQrStUvWx',
    sendgrid: 'SG.1234567890abcdefghijklm.nopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ',
    twilio: 'SK1234567890abcdef1234567890abcdef',
    openai: 'sk-proj-1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ',
    google: 'AIzaSyD1234567890_abcdefghijklmnopqrstuvw',
    firebase: 'AAAA1234567890:abcdefghijklmnopqrstuvwxyz-ABCDEFGHIJKLMNOPQRSTU',
    azure: 'DefaultEndpointsProtocol=https;AccountName=myaccount;AccountKey=abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890==;EndpointSuffix=core.windows.net'
  },

  // OAuth Credentials
  oauth: {
    clientId: 'my-oauth-client-id-12345',
    clientSecret: 'my-oauth-client-secret-67890-abcdef',
    redirectUri: 'https://example.com/oauth/callback'
  },

  // JWT Configuration
  jwt: {
    secret: 'super-secret-jwt-key-that-should-not-be-hardcoded',
    expiresIn: '24h',
    algorithm: 'HS256'
  },

  // Encryption Keys
  encryption: {
    key: 'a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6',
    iv: 'q1w2e3r4t5y6u7i8',
    algorithm: 'aes-256-cbc',
    privateKey: `-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEA1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMN
OPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQR
STUVWXYZabcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUV
-----END RSA PRIVATE KEY-----`
  },

  // Email Configuration
  email: {
    service: 'gmail',
    user: 'system@company.com',
    password: 'EmailSecretPassword123!',
    smtpHost: 'smtp.gmail.com',
    smtpPort: 587
  },

  // Payment Gateway
  payment: {
    merchantId: 'merchant_abc123def456',
    merchantKey: 'mk_live_1234567890abcdefghijklmnopqrstuvwxyz',
    apiPassword: 'paymentApiPassword123!',
    webhookSecret: 'whsec_1234567890abcdefghijklmnopqrstuvwxyz'
  },

  // Social Media API Keys
  social: {
    twitterApiKey: 'twitter_api_key_1234567890abcdefghijklm',
    twitterApiSecret: 'twitter_api_secret_nopqrstuvwxyz1234567890ABCDEFGHIJK',
    twitterAccessToken: '1234567890-abcdefghijklmnopqrstuvwxyzABCDEFGHIJ',
    twitterAccessSecret: 'twitter_access_secret_KLMNOPQRSTUVWXYZ12345',
    facebookAppId: '1234567890123456',
    facebookAppSecret: 'abcdef1234567890ghijklmnopqrstuv'
  },

  // Database Connection Strings
  connections: {
    mongodb: 'mongodb+srv://admin:MongoP@ssw0rd@cluster0.mongodb.net/mydb?retryWrites=true',
    redis: 'redis://:RedisPassword123@redis-server.example.com:6379/0',
    elasticsearch: 'https://elastic:ElasticPass123@es.example.com:9200'
  },

  // Admin Credentials
  admin: {
    username: 'superadmin',
    password: 'Admin123!@#',
    email: 'admin@example.com',
    apiKey: 'admin_key_xyz789abc456def123'
  }
};