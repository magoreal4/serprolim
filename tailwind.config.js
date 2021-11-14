module.exports = {
  purge: [
      './app/templates/**/*.html',
      './app/static/**/*.js'
  ],
  darkMode: false,
  theme: {
      extend: {
          height: theme => ({
              'screen90': '90vh',
              'screen75': '75vh',
              'screen/2': '50vh',
              'screen/3': 'calc(100vh / 3)',
              'screen/4': 'calc(100vh / 4)',
              'screen/5': 'calc(100vh / 5)',
              'screen400': '400px',
              'screen600': '600px',
              'screen800': '800px',
              'screen1000': '1000px'
            }),
          fontFamily: {
              'nunito': ['"Nunito"','sans-serif'],
              'noto': ['"Noto+Serif"','serif'],     
          },
          colors: {
              yellow: {
                  350: '#f9cc41'
              }

          }
      },
      container: {
          center: true,
      },
      zIndex: {
        '0': 0,
        '10': 10,
        '20': 20,
        '30': 30,
        '40': 40,
        '50': 50,
        '25': 25,
        '50': 50,
        '75': 75,
        '100': 100,
        'auto': 'auto',
        '10000':10000
      }
  },
  variants: {
      extend: {},
  },
  plugins: [],
}