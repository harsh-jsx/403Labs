# How Caller ID Spoofing Works - Technical Explanation

## 📞 The Phone Call Process

```
┌─────────────┐         ┌──────────────┐         ┌─────────────┐
│   Caller    │────────▶│  VoIP Service│────────▶│  Recipient  │
│  (You/Bot)  │         │  (Twilio)    │         │  (Victim)   │
└─────────────┘         └──────────────┘         └─────────────┘
     │                          │                        │
     │                          │                        │
     │ 1. Request Call          │                        │
     │    to: +1234567890       │                        │
     │    from: +1987654321     │                        │
     │                          │                        │
     │                          │ 2. Create SIP Message  │
     │                          │    From: +1987654321   │
     │                          │    To: +1234567890    │
     │                          │                        │
     │                          │ 3. Send to Phone       │
     │                          │    Network             │
     │                          │                        │
     │                          │                        │ 4. Display Caller ID
     │                          │                        │    Shows: +1987654321
     │                          │                        │    (Trusts SIP header)
```

## 🔍 The Key: SIP Protocol

**SIP (Session Initiation Protocol)** is the protocol used for VoIP calls. It's like HTTP for phone calls.

### SIP Message Structure

```
INVITE sip:+1234567890@phone-network.com SIP/2.0
Via: SIP/2.0/UDP voip-service.com:5060
From: <sip:+1987654321@voip-service.com>;tag=abc123
To: <sip:+1234567890@phone-network.com>
Call-ID: xyz789@voip-service.com
CSeq: 1 INVITE
Contact: <sip:+1987654321@voip-service.com>
Content-Type: application/sdp
```

**The `From:` header is what appears as caller ID!**

## ⚙️ How It Works in Code

### Legitimate Service (Twilio)

```python
# You can only use verified numbers
call = client.calls.create(
    to="+1234567890",           # Recipient
    from_="+1987654321",        # Must be verified with Twilio
    url="http://callback-url"
)
```

**What happens:**

1. Twilio checks if `+1987654321` is verified in your account
2. If verified ✅ → Call proceeds, caller ID shows `+1987654321`
3. If not verified ❌ → Call fails with error

### Malicious Service (Unverified Provider)

```python
# Malicious service doesn't verify
call = malicious_client.calls.create(
    to="+1234567890",           # Recipient
    from_="+15551234567",       # ANY number works!
    url="http://callback-url"
)
```

**What happens:**

1. Malicious service doesn't verify the number
2. Sets `From:` header to any number you want
3. Phone network trusts the SIP header
4. Recipient sees the spoofed number ✅ (for the scammer)

## 🛡️ Why Phone Networks Trust It

1. **Legacy System:**

   - Phone systems were designed before spoofing was common
   - They trust the caller ID from the SIP header
   - No built-in verification

2. **No Universal Verification:**

   - There's no global database of "who owns this number"
   - Each carrier manages their own numbers
   - Cross-carrier verification is difficult

3. **Trust-Based Model:**
   - Phone networks assume caller ID is accurate
   - They display what's in the SIP header
   - No validation step

## 🔒 The Solution: STIR/SHAKEN

**STIR/SHAKEN** (Secure Telephone Identity Revisited / Signature-based Handling of Asserted information using toKENs) is a new protocol being rolled out.

### How STIR/SHAKEN Works

```
┌─────────────┐         ┌──────────────┐         ┌─────────────┐
│   Caller    │────────▶│  VoIP Service│────────▶│  Recipient  │
│             │         │              │         │             │
└─────────────┘         └──────────────┘         └─────────────┘
                              │
                              │ 1. Sign the call with
                              │    cryptographic signature
                              │
                              │ 2. Attach token to SIP
                              │    message
                              │
                              │ 3. Phone network verifies
                              │    signature
                              │
                              │ 4. Shows verification
                              │    status to recipient
```

**Verification Levels:**

- ✅ **A (Attested):** Verified caller owns the number
- ✅ **B (Partially Attested):** Verified caller is authorized
- ⚠️ **C (Gateway):** Call passed through gateway, less certain
- ❌ **No verification:** Unverified call (likely spoofed)

## 📊 Comparison Table

| Feature                 | Legitimate Service         | Malicious Service       |
| ----------------------- | -------------------------- | ----------------------- |
| **Number Verification** | ✅ Required                | ❌ None                 |
| **Audit Trail**         | ✅ Yes                     | ❌ No                   |
| **Compliance**          | ✅ Follows regulations     | ❌ Often violates       |
| **Accountability**      | ✅ Tracked                 | ❌ Anonymous            |
| **Use Case**            | Business, notifications    | Scams, harassment       |
| **Cost**                | Higher (compliance)        | Lower (no verification) |
| **Legal**               | ✅ Legal (with disclosure) | ❌ Often illegal        |

## 🎯 Key Technical Points

1. **SIP Header Manipulation:**

   - The `From:` field in SIP can be set to any value
   - Phone networks display this as caller ID
   - No validation by default

2. **Verification is Optional:**

   - Legitimate services verify (Twilio)
   - Malicious services don't verify
   - Phone networks can't tell the difference

3. **Trust-Based System:**

   - Phone networks trust caller ID
   - Recipients trust what they see
   - No built-in security

4. **New Solutions:**
   - STIR/SHAKEN adds verification
   - Cryptographic signatures prove ownership
   - Being rolled out globally

## 🔬 Experiment Ideas

1. **Test with Twilio:**

   - Try using an unverified number → Should fail
   - Use a verified number → Should work
   - Shows the difference

2. **Analyze SIP Messages:**

   - Use Wireshark to capture SIP traffic
   - See the `From:` header in action
   - Understand the protocol

3. **Compare Services:**
   - Legitimate: Twilio, Vonage, etc.
   - Research malicious services (for educational purposes)
   - Compare verification requirements

## 📚 Further Reading

- [SIP Protocol RFC 3261](https://tools.ietf.org/html/rfc3261)
- [STIR/SHAKEN Technical Specification](https://www.atis.org/stir-shaken/)
- [FCC Call Authentication](https://www.fcc.gov/call-authentication)
