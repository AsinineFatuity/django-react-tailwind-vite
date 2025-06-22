WEBPACK_DEV_CONTENT = """
const path = require("path");
const webpack = require("webpack");
const HtmlWebpackPlugin = require("html-webpack-plugin");
const LiveReloadPlugin = require("webpack-livereload-plugin");
const dotenv = require("dotenv").config({
  path: "./frontend/environments/.env.development",
});

const {
  commonOutput,
  commonResolve,
  commonRules,
} = require("./webpack.common.js");

module.exports = {
  entry: ["./frontend/index.tsx"],
  mode: "development",
  output: commonOutput,
  devtool: "inline-source-map",
  devServer: {
    hot: true, // Tell the dev-server we're using HMR
    devMiddleware: {
      writeToDisk: true, // Write files to disk in dev mode, so Django can serve the assets
    },
    compress: true, // Enable gzip compression for everything served by wds
  },
  resolve: commonResolve,
  module: {
    rules: commonRules,
  },
  plugins: [
    new webpack.DefinePlugin({
      "process.env": JSON.stringify(dotenv.parsed),
    }),
    new HtmlWebpackPlugin({
      template: path.resolve(__dirname, "../templates/home.html"),
      inject: true,
    }),
    new LiveReloadPlugin(),
  ],
};

"""
