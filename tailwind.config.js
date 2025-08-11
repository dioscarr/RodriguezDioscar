/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./index.html", "./src/**/*.{js,ts,jsx,tsx}"],
  darkMode: "class",
  theme: {
    extend: {
      fontFamily: {
        sans: [
          "Inter",
          "ui-sans-serif",
          "system-ui",
          "Segoe UI",
          "Roboto",
          "Helvetica",
          "Arial",
          "Apple Color Emoji",
          "Segoe UI Emoji",
          "Segoe UI Symbol"
        ]
      },
      colors: {
        brand: {
          DEFAULT: "#2563eb",
          light: "#60a5fa",
          dark: "#1d4ed8"
        }
      },
      boxShadow: {
        soft: "0 10px 25px -10px rgba(0,0,0,0.25)"
      }
    }
  },
  plugins: []
};