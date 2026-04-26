/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        'anthracite': '#121212',
        'rose-gold': '#E4B1AB',
        'deep-violet': '#2D0054', // Le violet sombre des éclairs
      },
      backgroundImage: {
        // Le dégradé du fond : Noir vers un centre violet très sombre
        'main-bg': 'radial-gradient(circle at center, #1a0033 0%, #000000 100%)',
      }
    },
  },
  plugins: [],
}