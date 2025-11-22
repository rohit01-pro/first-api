from playwright.sync_api import sync_playwright, expect

def verify_frontend():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        try:
            # Navigate to the frontend dev server
            page.goto("http://localhost:5173")

            # Wait for the main content to load.
            # Based on HomePage.jsx, there is a text "Current Products"
            expect(page.get_by_text("Current Products")).to_be_visible()

            # Take a screenshot of the home page
            page.screenshot(path="/app/verification/home_page_dev.png")
            print("Screenshot taken")

        except Exception as e:
            print(f"Error: {e}")
        finally:
            browser.close()

if __name__ == "__main__":
    verify_frontend()
