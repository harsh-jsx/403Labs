# Educational Phone Calling Demo

**⚠️ IMPORTANT: This is for EDUCATIONAL PURPOSES ONLY**

This demo explains how caller ID spoofing works using VoIP (Voice over IP) services. It's designed for classroom demonstrations to help students understand the technology behind phone spoofing and the security implications.

## ⚖️ Legal and Ethical Warning

**Caller ID spoofing can be illegal in many jurisdictions when used for:**

- Fraud or scams
- Harassment or stalking
- Impersonation
- Violating telemarketing regulations

**This demo uses Twilio, which:**

- Only allows verified phone numbers
- Provides audit trails
- Complies with telecommunications regulations
- Is used for legitimate business purposes

**Always:**

- Check local laws before using
- Only use for legitimate, educational purposes
- Never use to deceive, harass, or defraud
- Respect privacy and consent

## 🎓 Educational Purpose

This demo is designed to help students understand:

1. How VoIP services work
2. How caller ID is transmitted in phone calls
3. Why caller ID spoofing is possible
4. The difference between legitimate and malicious services
5. Security implications of phone systems

## 📋 Prerequisites

1. **Python 3.7+** installed
2. **Twilio Account** (free trial available):
   - Sign up at https://www.twilio.com/try-twilio
   - Get your Account SID and Auth Token
   - Purchase a phone number (or use trial number)

## 🚀 Setup

1. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

2. **Configure your Twilio credentials:**

   ```bash
   # Option 1: Copy the example config and edit it
   cp config.example.json config.json
   # Then edit config.json with your credentials

   # Option 2: Set environment variables
   export TWILIO_ACCOUNT_SID="your_account_sid"
   export TWILIO_AUTH_TOKEN="your_auth_token"
   export TWILIO_PHONE_NUMBER="+1234567890"
   ```

3. **Run the demo:**
   ```bash
   python phone_demo.py
   ```

## 🔍 How It Works

### Technical Explanation

1. **SIP Protocol (Session Initiation Protocol):**

   - When making a VoIP call, the caller ID is sent in the SIP header
   - The `From` field contains the caller ID information
   - Phone networks display this information to the recipient

2. **Legitimate Services (Twilio):**

   - Verify phone numbers before allowing their use
   - Only let you use numbers you own or have verified
   - Provide audit trails and compliance features
   - Used for legitimate business purposes (call centers, notifications, etc.)

3. **Malicious Services:**

   - Don't verify caller IDs
   - Allow any number to be used
   - Often operate from jurisdictions with lax regulations
   - Used by scammers for fraud and harassment

4. **Why It Works:**
   - Phone networks trust the caller ID from the SIP header
   - There's no universal verification system
   - Legacy phone systems weren't designed with security in mind
   - STIR/SHAKEN is a new protocol trying to fix this

### The Code

The key part is in the `make_call()` function:

```python
call = self.client.calls.create(
    to=to_number,
    from_=from_number,  # This is what appears as caller ID
    url="http://your-server.com/call-handler",
    method='POST'
)
```

The `from_` parameter sets what appears as the caller ID. With Twilio, you can only use verified numbers. Malicious services don't verify, allowing any number.

## 📚 Classroom Discussion Points

1. **Why is caller ID spoofing possible?**

   - Legacy phone systems trust caller ID information
   - No universal verification system exists
   - VoIP makes it easier to manipulate caller ID

2. **What's the difference between legitimate and malicious use?**

   - Legitimate: Verified numbers, audit trails, compliance
   - Malicious: Unverified numbers, no accountability

3. **How can we protect against spoofing?**

   - STIR/SHAKEN protocol (new verification standard)
   - Call blocking apps
   - Being skeptical of unknown callers
   - Never giving personal information over the phone

4. **What are the legal implications?**
   - Illegal for fraud, harassment, impersonation
   - Legal for legitimate business (with proper disclosure)
   - Varies by jurisdiction

## 🛠️ Advanced: Running with Webhooks

For a full demo with actual call handling, you'll need:

1. **A publicly accessible server** (or use ngrok for local testing):

   ```bash
   ngrok http 5000
   ```

2. **Update the callback URL** in `phone_demo.py`:

   ```python
   url=f"https://your-ngrok-url.ngrok.io/call-handler"
   ```

3. **Run the Flask server**:
   ```python
   # Add to phone_demo.py:
   if __name__ == "__main__":
       app.run(port=5000, debug=True)
   ```

## 🔒 Security Notes

- Never commit `config.json` with real credentials
- Use environment variables in production
- Keep your Twilio Auth Token secret
- Only use verified phone numbers

## 📖 Additional Resources

- [Twilio Documentation](https://www.twilio.com/docs)
- [STIR/SHAKEN Protocol](https://www.fcc.gov/call-authentication)
- [FCC on Caller ID Spoofing](https://www.fcc.gov/spoofing)

## 🤝 Contributing

This is an educational demo. Suggestions for improvements are welcome, but remember:

- Keep it educational
- Include legal/ethical warnings
- Focus on understanding, not exploitation

## 📝 License

This educational demo is provided as-is for educational purposes only. Use responsibly and in compliance with all applicable laws.
