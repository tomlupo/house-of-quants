/** @type {import('tailwindcss').Config} */

// House of Quants Brand - Tailwind Configuration
// A hand mirror of assets/css-variables.css, which owns every value.
// tests/test_brand_pack.py fails if a colour here is missing from the owner.
// Dark only: set the page to bg-background with text-foreground.
// Load Roboto (300, 400, 700) and Roboto Mono from Google Fonts in the app.

module.exports = {
  theme: {
    extend: {
      colors: {
        // Surfaces: deep navy
        background: '#060b12',
        surface: { DEFAULT: '#0b1420', soft: '#0e1a29' },
        header: { DEFAULT: '#08111c', glass: 'rgba(5, 10, 17, 0.94)' },

        // Text
        foreground: '#eaf6ff',
        heading: '#f5fbff',
        emphasis: '#f2faff',
        lead: '#cde9f8',
        muted: '#9eb5c6',
        'on-accent': '#04101a',

        // Accent: the sky blue of the mark
        primary: '#77cfff',
        accent: { DEFAULT: '#43b8ff', from: '#2f9fe8', to: '#6bcfff' },

        // Borders
        border: {
          DEFAULT: 'rgba(130, 205, 255, 0.16)',
          hover: 'rgba(102, 198, 255, 0.36)',
          faint: 'rgba(127, 207, 255, 0.12)',
        },

        // Semantic (derived)
        success: '#4CC08A',
        warning: '#E0A458',
        error: '#E36358',

        // Chart series, in order
        chart: {
          1: '#77cfff',
          2: '#B39DDB',
          3: '#4FD1C5',
          4: '#F48FB1',
          5: '#9eb5c6',
        },
      },

      fontFamily: {
        sans: ['Roboto', '-apple-system', 'BlinkMacSystemFont', 'Segoe UI', 'system-ui', 'sans-serif'],
        mono: ['Roboto Mono', 'ui-monospace', 'SF Mono', 'Menlo', 'Consolas', 'monospace'],
      },

      fontWeight: {
        light: '300',
        normal: '400',
        bold: '700',
        title: '720',
      },

      fontSize: {
        title: ['clamp(2.6rem, 7vw, 5.5rem)', { lineHeight: '0.96', letterSpacing: '-0.055em' }],
        lead: 'clamp(1.15rem, 2.3vw, 1.55rem)',
        card: '0.9rem',
        kicker: ['0.78rem', { letterSpacing: '0.14em' }],
      },

      letterSpacing: {
        heading: '-0.025em',
      },

      maxWidth: {
        content: '1280px',
        copy: '42rem',
      },

      borderRadius: {
        sm: '8px',
        md: '10px',
        lg: '16px',
        xl: '22px',
      },

      backgroundImage: {
        page: 'linear-gradient(180deg, #07101a 0%, #050911 72%)',
        'page-glow': 'radial-gradient(circle at 50% 0%, rgba(39, 129, 191, 0.13), transparent 32rem)',
        card: 'linear-gradient(180deg, rgba(15, 28, 43, 0.92), rgba(8, 17, 28, 0.92))',
        accent: 'linear-gradient(135deg, #2f9fe8, #6bcfff)',
      },

      boxShadow: {
        glow: '0 0 28px rgba(61, 182, 255, 0.18)',
        'card-hover': '0 18px 45px rgba(0, 0, 0, 0.24)',
        visual: '0 18px 54px rgba(0, 0, 0, 0.32)',
      },
    },
  },
};
