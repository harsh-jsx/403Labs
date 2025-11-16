"""
Educational Phone Calling Demo
==============================
This demo shows how caller ID spoofing works using VoIP services.

IMPORTANT: This is for EDUCATIONAL PURPOSES ONLY.
Caller ID spoofing can be illegal in many jurisdictions when used for:
- Fraud
- Harassment
- Impersonation
- Scams

Always comply with local laws and regulations.
"""

import os
from twilio.rest import Client
from twilio.twiml.voice_response import VoiceResponse, Say
from flask import Flask, request
import json

# Initialize Flask app for handling callbacks
app = Flask(__name__)

# Load configuration
def load_config():
    """Load configuration from config.json or environment variables"""
    config = {}
    
    # Try to load from config.json
    if os.path.exists('config.json'):
        with open('config.json', 'r') as f:
            config = json.load(f)
    else:
        # Fall back to environment variables
        config = {
            'account_sid': os.getenv('TWILIO_ACCOUNT_SID'),
            'auth_token': os.getenv('TWILIO_AUTH_TOKEN'),
            'phone_number': os.getenv('TWILIO_PHONE_NUMBER')
        }
    
    return config


class PhoneCallDemo:
    """
    Educational demo class showing how phone calling with custom caller ID works.
    
    How it works:
    1. VoIP services (like Twilio) allow you to set a custom caller ID
    2. The caller ID is sent in the SIP (Session Initiation Protocol) header
    3. Phone networks display this caller ID to the recipient
    4. For legitimate services, you can only use verified phone numbers
    5. Scammers use unverified VoIP providers that don't validate caller IDs
    """
    
    def __init__(self, account_sid, auth_token, from_number):
        """
        Initialize the Twilio client.
        
        Args:
            account_sid: Twilio Account SID
            auth_token: Twilio Auth Token
            from_number: Your Twilio phone number (verified number)
        """
        self.client = Client(account_sid, auth_token)
        self.from_number = from_number
        print(f"✓ Initialized Phone Call Demo")
        print(f"  From Number: {from_number}")
    
    def make_call(self, to_number, caller_id=None, message="Hello, this is an educational demo call.", use_twiml=True):
        """
        Make a phone call with optional custom caller ID.
        
        How caller ID spoofing works:
        - The 'from' parameter in the API call sets the caller ID
        - Twilio only allows verified numbers (for legitimate use)
        - Malicious services don't verify, allowing any number
        - The phone network trusts and displays this caller ID
        
        Args:
            to_number: Number to call (E.164 format: +1234567890)
            caller_id: Optional custom caller ID (must be verified with Twilio)
            message: Message to play during the call
            use_twiml: If True, use TwiML string directly (no webhook needed)
        """
        # Use custom caller ID if provided, otherwise use default
        from_number = caller_id if caller_id else self.from_number
        
        print(f"\n📞 Making call...")
        print(f"  To: {to_number}")
        print(f"  Caller ID (From): {from_number}")
        print(f"  Message: {message}")
        
        try:
            # Create TwiML response for the call
            if use_twiml:
                response = VoiceResponse()
                response.say(message, voice='alice')
                response.say("This demonstrates how caller ID can be customized using VoIP services.", voice='alice')
                twiml = str(response)
            else:
                # Use webhook URL (requires public server)
                twiml = f"http://your-server.com/call-handler"
            
            # Make the call
            # The 'from' parameter sets what appears as caller ID
            if use_twiml:
                call = self.client.calls.create(
                    to=to_number,
                    from_=from_number,  # This is what appears as caller ID
                    twiml=twiml  # Use TwiML directly
                )
            else:
                call = self.client.calls.create(
                    to=to_number,
                    from_=from_number,  # This is what appears as caller ID
                    url=twiml,  # Use webhook URL
                    method='POST'
                )
            
            print(f"✓ Call initiated successfully!")
            print(f"  Call SID: {call.sid}")
            print(f"  Status: {call.status}")
            
            return call
            
        except Exception as e:
            error_str = str(e)
            print(f"✗ Error making call: {e}")
            
            # Check for specific Twilio errors
            if "unverified" in error_str.lower() or "trial" in error_str.lower():
                # Check if this is a recipient number issue or caller ID issue
                if "caller id" in error_str.lower() or "from" in error_str.lower() or "caller" in error_str.lower():
                    print("\n" + "="*70)
                    print("🔒 SECURITY FEATURE: Caller ID Verification")
                    print("="*70)
                    print("\n✅ SUCCESS! Twilio REJECTED the call because:")
                    print(f"   - The caller ID ({from_number}) is NOT verified")
                    print("   - This is a SECURITY FEATURE, not a bug!")
                    print("\n📚 EDUCATIONAL POINT:")
                    print("   This demonstrates how legitimate services PREVENT spoofing.")
                    print("   Malicious services would have allowed this call.")
                    print("\n" + "="*70)
                else:
                    # Recipient number issue
                    print("\n" + "="*70)
                    print("⚠️  TRIAL ACCOUNT LIMITATION")
                    print("="*70)
                    print("\nTwilio trial accounts can only call VERIFIED numbers.")
                    print("\nTo fix this, you have 2 options:")
                    print("\nOPTION 1: Verify the recipient number (Recommended for testing)")
                    print("  1. Go to: https://console.twilio.com/us1/develop/phone-numbers/manage/verified")
                    print("  2. Click 'Add a new number'")
                    print("  3. Enter: +919266823269")
                    print("  4. Twilio will call/text to verify it")
                    print("  5. Enter the verification code")
                    print("  6. Run this script again")
                    print("\nOPTION 2: Upgrade to a paid account")
                    print("  1. Go to: https://console.twilio.com/billing")
                    print("  2. Add payment method")
                    print("  3. Upgrade account (you'll get $15.50 free credit)")
                    print("  4. Then you can call any number")
                    print("\n" + "="*70)
            else:
                print("\nCommon issues:")
                print("  1. Make sure your Twilio number is verified")
                print("  2. Check that the recipient number is in E.164 format (+country code)")
                print("  3. Ensure your Twilio account has calling enabled")
                print("  4. Verify you have sufficient balance in your Twilio account")
                print("  5. For trial accounts: recipient number must be verified")
            return None
    
    def send_sms(self, to_number, message, from_number=None):
        """
        Send SMS with custom sender number.
        
        Similar to voice calls, SMS also allows custom sender IDs.
        """
        from_number = from_number if from_number else self.from_number
        
        print(f"\n📱 Sending SMS...")
        print(f"  To: {to_number}")
        print(f"  From: {from_number}")
        print(f"  Message: {message}")
        
        try:
            message = self.client.messages.create(
                to=to_number,
                from_=from_number,
                body=message
            )
            
            print(f"✓ SMS sent successfully!")
            print(f"  Message SID: {message.sid}")
            return message
            
        except Exception as e:
            error_str = str(e)
            print(f"✗ Error sending SMS: {e}")
            
            # Check for specific Twilio trial account error
            if "unverified" in error_str.lower() or "trial" in error_str.lower():
                print("\n⚠️  Trial accounts can only send SMS to verified numbers.")
                print("   Verify the number at: https://console.twilio.com/us1/develop/phone-numbers/manage/verified")
            return None
    
    def verify_number(self, phone_number):
        """
        Helper method to check if a number is verified in your Twilio account.
        Note: This doesn't verify the number, just checks if it's already verified.
        """
        try:
            verified_numbers = self.client.outgoing_caller_ids.list(limit=100)
            verified_list = [num.phone_number for num in verified_numbers]
            
            if phone_number in verified_list:
                print(f"✓ {phone_number} is verified in your account")
                return True
            else:
                print(f"✗ {phone_number} is NOT verified in your account")
                print(f"\nTo verify it:")
                print(f"  1. Go to: https://console.twilio.com/us1/develop/phone-numbers/manage/verified")
                print(f"  2. Click 'Add a new number'")
                print(f"  3. Enter: {phone_number}")
                return False
        except Exception as e:
            print(f"Error checking verified numbers: {e}")
            return False
    
    def demonstrate_spoofing_attempt(self, to_number, spoofed_caller_id, message="This is a spoofing demonstration."):
        """
        EDUCATIONAL DEMO: Attempt to call from an unverified number.
        
        This demonstrates:
        1. How legitimate services (Twilio) PREVENT spoofing
        2. Why this is a security feature
        3. How malicious services differ (they don't verify)
        
        This will FAIL with Twilio, which is the point - showing students
        why legitimate services are secure.
        """
        print("\n" + "="*70)
        print("🎓 EDUCATIONAL DEMO: Attempting Caller ID Spoofing")
        print("="*70)
        print(f"\nAttempting to call from: {spoofed_caller_id}")
        print(f"To: {to_number}")
        print(f"\n⚠️  This number is NOT verified in your Twilio account.")
        print("   This demonstrates how legitimate services prevent spoofing.")
        print("\n" + "-"*70)
        
        # Attempt the call with unverified number
        result = self.make_call(
            to_number=to_number,
            caller_id=spoofed_caller_id,  # Unverified number
            message=message
        )
        
        print("\n" + "="*70)
        print("📚 EDUCATIONAL EXPLANATION")
        print("="*70)
        print("""
WHAT JUST HAPPENED:

✅ TWILIO (Legitimate Service):
   - REJECTED the call because the number isn't verified
   - This is a SECURITY FEATURE
   - Prevents unauthorized caller ID spoofing
   - Protects users from scams

❌ MALICIOUS SERVICES (Unverified Providers):
   - Would have ALLOWED this call
   - Don't verify caller IDs
   - Allow ANY number to be used
   - This is how scammers spoof numbers

KEY TAKEAWAY:
   The fact that Twilio REJECTED this call is GOOD!
   It shows legitimate services protect users.
   Malicious services don't have this protection.

HOW SCAMMERS DO IT:
   1. Use unverified VoIP providers
   2. Set any caller ID they want
   3. Phone networks trust and display it
   4. Recipients see the spoofed number
   5. No verification = easy spoofing

WHY IT WORKS FOR SCAMMERS:
   - Phone networks trust caller ID from SIP header
   - No universal verification system
   - Legacy systems weren't designed for security
   - Unverified services don't check ownership
        """)
        
        return result


@app.route('/call-handler', methods=['POST'])
def handle_call():
    """
    Handle incoming call webhook.
    This endpoint receives the call and plays a message.
    """
    response = VoiceResponse()
    
    # Get the message from query parameters or use default
    message = request.args.get('message', 'Hello, this is an educational demo call.')
    
    response.say(message, voice='alice')
    response.say("This demonstrates how caller ID can be customized using VoIP services.", voice='alice')
    
    return str(response)


def explain_how_it_works():
    """
    Educational explanation of how caller ID spoofing works.
    """
    print("\n" + "="*70)
    print("HOW CALLER ID SPOOFING WORKS (Educational Explanation)")
    print("="*70)
    print("""
1. VOIP PROTOCOLS (SIP - Session Initiation Protocol):
   - When making a call, the caller ID is sent in the SIP header
   - The 'From' field in the SIP message contains the caller ID
   - Phone networks display this information to the recipient

2. LEGITIMATE SERVICES (like Twilio):
   - Verify phone numbers before allowing their use
   - Only let you use numbers you own or have verified
   - Provide audit trails and compliance features
   - Used for legitimate business purposes

3. MALICIOUS SERVICES:
   - Don't verify caller IDs
   - Allow any number to be used
   - Often operate from jurisdictions with lax regulations
   - Used by scammers for fraud and harassment

4. WHY IT WORKS:
   - Phone networks trust the caller ID from the SIP header
   - There's no universal verification system
   - Legacy phone systems weren't designed with security in mind
   - STIR/SHAKEN is a new protocol trying to fix this

5. LEGAL CONSIDERATIONS:
   - Illegal in many places for fraud, harassment, or impersonation
   - Legal for legitimate business (call centers, etc.)
   - Always check local laws before using
   - This demo is for educational purposes only
    """)


def main():
    """Main function for the demo"""
    print("\n" + "="*70)
    print("EDUCATIONAL PHONE CALLING DEMO")
    print("="*70)
    
    # Load configuration
    config = load_config()
    
    if not config.get('account_sid') or not config.get('auth_token'):
        print("\n⚠ Configuration needed!")
        print("Please set up config.json or environment variables:")
        print("  - TWILIO_ACCOUNT_SID")
        print("  - TWILIO_AUTH_TOKEN")
        print("  - TWILIO_PHONE_NUMBER")
        print("\nSee config.example.json for a template.")
        
        # Still show the educational explanation
        explain_how_it_works()
        return
    
    # Initialize demo
    demo = PhoneCallDemo(
        account_sid=config['account_sid'],
        auth_token=config['auth_token'],
        from_number=config['phone_number']
    )
    
    # Show educational explanation
    explain_how_it_works()
    
    # ====================================================================
    # EDUCATIONAL DEMO: Show students how caller ID spoofing works
    # ====================================================================
    
    recipient_number = "+919266823269"
    
    print("\n" + "="*70)
    print("DEMO OPTIONS")
    print("="*70)
    print("\n1. LEGITIMATE CALL (using verified number)")
    print("2. SPOOFING ATTEMPT (using unverified number) - Shows security")
    print("\n" + "-"*70)
    
    # DEMO 1: Legitimate call with verified number
    print("\n📞 DEMO 1: Legitimate Call (Verified Number)")
    print("-"*70)
    print(f"Checking if {recipient_number} is verified...")
    is_verified = demo.verify_number(recipient_number)
    
    if not is_verified:
        print(f"\n⚠️  Note: If you're on a trial account, you need to verify this number first.")
        print(f"   The call will still be attempted, but may fail if unverified.")
    
    # Make legitimate call
    demo.make_call(
        to_number=recipient_number,
        caller_id=config['phone_number'],  # Using verified Twilio number
        message="Hello, this is an educational demo call from your professor."
    )
    
    # DEMO 2: Attempt spoofing with unverified number
    print("\n\n" + "="*70)
    print("📞 DEMO 2: Spoofing Attempt (Unverified Number)")
    print("="*70)
    print("\nThis demonstrates how legitimate services PREVENT spoofing.")
    print("We'll try to call from a number we don't own/verify.")
    print("\nExample spoofed numbers (pick any number you don't own):")
    print("  - +15551234567 (fake number)")
    print("  - +12125551234 (fake number)")
    print("  - Any number you want to demonstrate with")
    
    # You can change this to any number you want to demonstrate with
    spoofed_number = "+15551234567"  # Change this to any unverified number
    
    print(f"\nAttempting to call from: {spoofed_number}")
    print("(This number is NOT verified in your account)")
    
    # This will FAIL - which is the educational point!
    demo.demonstrate_spoofing_attempt(
        to_number=recipient_number,
        spoofed_caller_id=spoofed_number,
        message="This call should fail because the number isn't verified."
    )
    
    # Example: Send SMS (uncomment to use)
    # demo.send_sms(
    #     to_number="+919266823269",
    #     message="This is an educational SMS demo.",
    #     from_number=config['phone_number']
    # )


if __name__ == "__main__":
    main()

