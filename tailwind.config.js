module.exports = {
  purge:  ['layouts/**/*.html'],
  darkMode: false, // or 'media' or 'class'
  theme: {
    extend: {
      scale: {
        '102':'1.02'
      },
      colors: {
        darkGray: '#171721',
        lightGray:'#23232d',
        gray1:'#7a828f',
        gray2:'#23232d',
        blue1:'#262b4c',
        lightBlue:'#02ffe7'
    }
  }
  },
  variants: {
    extend: {},
  },
  plugins: []
}
