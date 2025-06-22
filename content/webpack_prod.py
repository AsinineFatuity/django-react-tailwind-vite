WEBPACK_PROD_CONTENT = r"""
const path = require("path");
const webpack = require("webpack");
const HtmlWebpackPlugin = require("html-webpack-plugin");
const MiniCssExtractPlugin = require("mini-css-extract-plugin");
const CssMinimizerPlugin = require("css-minimizer-webpack-plugin");
const TerserPlugin = require("terser-webpack-plugin");
const dotenv = require("dotenv").config({
  path: "./frontend/environments/.env.production",
});

const {
  commonOutput,
  commonResolve,
  commonRules,
} = require("./webpack.common.js");

module.exports = {
  entry: ["./frontend/index.tsx"], // Path to our input file
  mode: "production",
  output: {
    ...commonOutput,
  },
  devtool: "source-map",
  devServer: {
    devMiddleware: {
      writeToDisk: true,
    },
    compress: true,
  },
  resolve: commonResolve,
  module: {
    rules: [
      ...commonRules,
      {
        test: /\.css$/,
        use: [MiniCssExtractPlugin.loader, "css-loader"],
      },
    ],
  },
  plugins: [
    new webpack.DefinePlugin({
      "process.env": JSON.stringify(dotenv.parsed),
    }),
    new HtmlWebpackPlugin({
      template: path.resolve(__dirname, "../templates/index.html"),
    }),
    new MiniCssExtractPlugin({
      filename: "[name].css",
      chunkFilename: "[id].css",
    }),
  ],
  optimization: {
    minimize: true,
    minimizer: [
      new TerserPlugin({
        terserOptions: {
          format: {
            comments: false,
          },
          compress: {
            drop_console: true,
          },
        },
        extractComments: false,
      }),
      new CssMinimizerPlugin(),
    ],
  },
};

"""
