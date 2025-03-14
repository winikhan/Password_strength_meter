import re
import streamlit as st

def check_password_strength(password):
    score = 0
    feedback = []
    
    # Check length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")
    
    # Check for uppercase letters
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("Include at least one uppercase letter.")
    
    # Check for lowercase letters
    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Include at least one lowercase letter.")
    
    # Check for digits
    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("Include at least one number.")
    
    # Check for special characters
    if re.search(r'[!@#$%^&*]', password):
        score += 1
    else:
        feedback.append("Include at least one special character (!@#$%^&*).")
    
    # Determine strength level
    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Moderate"
    else:
        strength = "Strong"
    
    return strength, feedback

def main():
    st.title("🔐 Password Strength Meter")
    password = st.text_input("Enter your password:", type="password")
    
    if st.button("Check Strength"):
        strength, feedback = check_password_strength(password)
        st.subheader(f"Password Strength: {strength}")
        
        if strength == "Weak":
            st.warning("Suggestions to improve your password:")
            for suggestion in feedback:
                st.write(f"- {suggestion}")
        elif strength == "Strong":
            st.success("Great job! Your password is strong.")

if __name__ == "__main__":
    main()
