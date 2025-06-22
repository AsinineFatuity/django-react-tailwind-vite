PACKAGE_JSON_CONTENT = """
{
  "scripts": {
    "start": "webpack-dev-server --config ./webpack/webpack.dev.js",
    "build": "webpack --mode production --config ./webpack/webpack.prod.js"
  },
  "dependencies": {
    "@babel/core": "^7.26.9",
    "@babel/preset-env": "^7.26.9",
    "@babel/preset-react": "^7.26.3",
    "@reduxjs/toolkit": "^2.6.1",
    "babel-loader": "^9.2.1",
    "bootstrap": "^5.3.3",
    "css-loader": "^7.1.2",
    "css-minimizer-webpack-plugin": "^7.0.0",
    "dotenv": "^16.4.7",
    "lodash": "^4.17.21",
    "mini-css-extract-plugin": "^2.9.2",
    "react": "^19.0.0",
    "react-bootstrap": "^2.10.9",
    "react-dom": "^19.0.0",
    "react-redux": "^9.2.0",
    "react-router-dom": "^7.2.0",
    "react-spinners": "^0.15.0",
    "react-toastify": "^11.0.5",
    "redux": "^5.0.1",
    "redux-thunk": "^3.1.0",
    "style-loader": "^4.0.0",
    "universal-cookie": "^7.2.2",
    "webpack": "^5.98.0",
    "webpack-cli": "^6.0.1"
  },
  "devDependencies": {
    "@babel/preset-typescript": "^7.26.0",
    "@types/jest": "^29.5.14",
    "@types/lodash": "^4.17.16",
    "@types/node": "^22.13.5",
    "@types/react": "^19.0.10",
    "@types/react-bootstrap": "^0.32.37",
    "@types/react-dom": "^19.0.4",
    "autoprefixer": "^10.4.20",
    "html-webpack-plugin": "^5.6.3",
    "prettier": "^3.5.3",
    "terser-webpack-plugin": "^5.3.11",
    "typescript": "^5.7.3",
    "webpack-dev-server": "^5.2.0",
    "webpack-livereload-plugin": "^3.0.2",
    "write-file-webpack-plugin": "^4.5.1"
  }
}
"""
