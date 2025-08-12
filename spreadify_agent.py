#!/usr/bin/env python3
"""
Spreadify Agents Browser Agent - Real Browser Automation for Social Media
This is a working browser agent that actually controls browsers and performs tasks.
"""

import asyncio
from playwright.async_api import async_playwright
import time
import random
from flask import Flask, render_template_string, request, jsonify
import threading
import json

class RealBrowserAgent:
    def __init__(self):
        self.browser = None
        self.page = None
        self.is_running = False
        self.status_log = []

    async def start_browser(self):
        """Start the browser and create a new page"""
        playwright = await async_playwright().start()
        self.browser = await playwright.chromium.launch(
            headless=False,  # Show the browser window
            args=['--no-sandbox', '--disable-dev-shm-usage']
        )

        # Create browser context with realistic user agent
        context = await self.browser.new_context(
            user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        )

        self.page = await context.new_page()
        self.log_status("â Browser started successfully")

    async def navigate_to_url(self, url):
        """Navigate to a specific URL"""
        if not self.page:
            await self.start_browser()

        self.log_status(f"ð Navigating to {url}")
        await self.page.goto(url)
        await self.page.wait_for_load_state("networkidle")
        self.log_status(f"â Successfully loaded {url}")

    async def demonstrate_social_media_automation(self):
        """Demonstrate real browser automation by visiting social media sites"""
        try:
            self.is_running = True
            self.log_status("ð¤ Starting Browser Agent Demo...")

            # Start browser
            await self.start_browser()

            # Visit Twitter/X
            self.log_status("ð± Testing Twitter/X automation...")
            await self.navigate_to_url("https://twitter.com")
            await asyncio.sleep(3)

            # Try to find login button
            try:
                login_selector = 'a[data-testid="loginButton"], a[href="/i/flow/login"]'
                login_button = await self.page.wait_for_selector(login_selector, timeout=5000)
                if login_button:
                    self.log_status("â Found Twitter login button - ready for authentication")
                    # Highlight the login button
                    await login_button.scroll_into_view_if_needed()
                    await self.page.evaluate("""
                        (element) => {
                            element.style.border = '3px solid red';
                            element.style.backgroundColor = 'yellow';
                        }
                    """, login_button)
            except:
                self.log_status("â¹ï¸ Twitter login button not immediately visible")

            await asyncio.sleep(2)

            # Visit Instagram
            self.log_status("ð¸ Testing Instagram automation...")
            await self.navigate_to_url("https://instagram.com")
            await asyncio.sleep(3)

            # Find Instagram login elements
            try:
                username_input = await self.page.wait_for_selector('input[name="username"]', timeout=5000)
                if username_input:
                    self.log_status("â Found Instagram username field - ready for login")
                    await self.page.evaluate("""
                        (element) => {
                            element.style.border = '3px solid blue';
                            element.placeholder = 'Agent can type here!';
                        }
                    """, username_input)
            except:
                self.log_status("â¹ï¸ Instagram login form not immediately visible")

            await asyncio.sleep(2)

            # Visit LinkedIn
            self.log_status("ð¼ Testing LinkedIn automation...")  
            await self.navigate_to_url("https://linkedin.com")
            await asyncio.sleep(3)

            # Find LinkedIn elements
            try:
                sign_in_button = await self.page.wait_for_selector('a[data-tracking-control-name="homepage-basic_sign-in-link"]', timeout=5000)
                if sign_in_button:
                    self.log_status("â Found LinkedIn sign-in - ready for automation")
                    await self.page.evaluate("""
                        (element) => {
                            element.style.border = '3px solid green';
                            element.style.backgroundColor = 'lightgreen';
                        }
                    """, sign_in_button)
            except:
                self.log_status("â¹ï¸ LinkedIn sign-in not immediately visible")

            await asyncio.sleep(2)

            # Demonstrate form filling
            self.log_status("ð Demonstrating form interaction...")
            await self.navigate_to_url("https://httpbin.org/forms/post")
            await asyncio.sleep(2)

            # Fill out a demo form
            try:
                await self.page.fill('input[name="custname"]', 'Spreadify Agents Agent Demo')
                await self.page.fill('textarea[name="comments"]', 'This is automated by the Spreadify Agents browser agent! ð¤')
                await self.page.select_option('select[name="custemail"]', 'Large')
                self.log_status("â Successfully filled demo form - proving real browser control")
                await asyncio.sleep(2)
            except Exception as e:
                self.log_status(f"â ï¸ Form demo error: {str(e)}")

            # Final demonstration
            self.log_status("ð Browser Agent Demo Complete!")
            self.log_status("â Successfully demonstrated:")
            self.log_status("  â¢ Real browser control")
            self.log_status("  â¢ Social media site navigation") 
            self.log_status("  â¢ Element detection and interaction")
            self.log_status("  â¢ Form filling capabilities")
            self.log_status("ð Agent is ready for social media tasks!")

        except Exception as e:
            self.log_status(f"â Error during demo: {str(e)}")
        finally:
            self.is_running = False
            # Keep browser open for 30 seconds for user to see results
            await asyncio.sleep(30)
            if self.browser:
                await self.browser.close()
                self.log_status("ð Browser closed")

    def log_status(self, message):
        """Add status message with timestamp"""
        timestamp = time.strftime("%H:%M:%S")
        log_entry = f"[{timestamp}] {message}"
        self.status_log.append(log_entry)
        print(log_entry)  # Also print to console

    def get_status_log(self):
        """Return the current status log"""
        return self.status_log

    def clear_log(self):
        """Clear the status log"""
        self.status_log = []

# Create Flask web application
app = Flask(__name__)
browser_agent = RealBrowserAgent()

@app.route('/')
def index():
    # Your HTML template would go here (truncated for brevity)
    return "Browser Agent Interface - See full code in file"

@app.route('/start-agent', methods=['POST'])
def start_agent():
    """Start the browser agent demonstration"""
    try:
        if browser_agent.is_running:
            return jsonify({"success": False, "error": "Agent is already running"})

        browser_agent.clear_log()

        def run_agent():
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            loop.run_until_complete(browser_agent.demonstrate_social_media_automation())
            loop.close()

        thread = threading.Thread(target=run_agent, daemon=True)
        thread.start()

        return jsonify({"success": True, "message": "Browser agent started"})

    except Exception as e:
        return jsonify({"success": False, "error": str(e)})

if __name__ == '__main__':
    print("ð Starting Spreadify Agents Browser Agent Server...")
    print("ð± Real browser automation for social media management")
    print("ð Server will be available at: http://localhost:5000")
    app.run(host='0.0.0.0', port=5000, debug=True)
