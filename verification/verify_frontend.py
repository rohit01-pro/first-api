from playwright.sync_api import sync_playwright, expect

def verify_frontend():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Navigate to the frontend
        # Since the backend failed to connect to mongo, it might have crashed or is just logging errors.
        # But the static file serving should work if the server is running.
        # Let's try to access the main page.
        try:
            page.goto("http://localhost:5002")

            # Wait for the title or some element
            expect(page).to_have_title("Vite + React") # Default title usually

            # Take a screenshot of the home page
            page.screenshot(path="/app/verification/home_page.png")
            print("Screenshot taken")

        except Exception as e:
            print(f"Error: {e}")
        finally:
            browser.close()

if __name__ == "__main__":
    verify_frontend()
