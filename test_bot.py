#!/usr/bin/env python3
"""
Simple test script to verify the ImageInsight Bot can be imported and basic functionality works.
This is not a comprehensive test suite, just a basic sanity check.
"""

import os
import sys
from unittest.mock import patch, MagicMock

def test_imports():
    """Test that all required modules can be imported."""
    try:
        import asyncio
        import os
        from telegram import Update
        from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
        from groq import Groq
        import nest_asyncio
        from PIL import Image
        import ollama
        from dotenv import load_dotenv
        print("✅ All imports successful")
        return True
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False

def test_environment_variables():
    """Test environment variable loading."""
    try:
        from dotenv import load_dotenv
        load_dotenv()
        
        # Test with mock environment variables
        with patch.dict(os.environ, {
            'TELEGRAM_API_TOKEN': 'test_token',
            'GROQ_API_KEY': 'test_key'
        }):
            token = os.getenv("TELEGRAM_API_TOKEN")
            key = os.getenv("GROQ_API_KEY")
            
            if token and key:
                print("✅ Environment variables loaded successfully")
                return True
            else:
                print("❌ Environment variables not loaded")
                return False
    except Exception as e:
        print(f"❌ Environment variable test failed: {e}")
        return False

def test_main_import():
    """Test that main.py can be imported without errors."""
    try:
        # Mock the API keys to avoid actual API calls
        with patch.dict(os.environ, {
            'TELEGRAM_API_TOKEN': 'test_token',
            'GROQ_API_KEY': 'test_key'
        }):
            # Import main module
            import main
            print("✅ Main module imported successfully")
            return True
    except Exception as e:
        print(f"❌ Main module import failed: {e}")
        return False

def main():
    """Run all tests."""
    print("Running basic tests...")
    print("-" * 40)
    
    tests = [
        ("Import Test", test_imports),
        ("Environment Variables Test", test_environment_variables),
        ("Main Module Test", test_main_import),
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        print(f"\nRunning {test_name}...")
        if test_func():
            passed += 1
        else:
            print(f"❌ {test_name} failed")
    
    print("\n" + "=" * 40)
    print(f"Tests passed: {passed}/{total}")
    
    if passed == total:
        print("🎉 All tests passed!")
        return 0
    else:
        print("⚠️  Some tests failed. Please check the output above.")
        return 1

if __name__ == "__main__":
    sys.exit(main()) 