WEBPACK_COMMON_CONTENT = r"""
const path = require("path");

const commonOutput = {
    filename: "index-bundle.js",
    path: path.resolve(__dirname, "../static"), // Path to our Django static directory (where compiled files go)
    publicPath: '../static/', // Public path where files are served from
    hotUpdateChunkFilename: 'hot/hot-update.js',
    hotUpdateMainFilename: 'hot/hot-update.json',
};

const commonResolve = {
    alias: {
        "@": path.resolve(__dirname, "src"),
        images: path.resolve(__dirname, "../frontend/src/images"),
    },
    extensions: [".*", ".js", ".jsx", ".ts", ".tsx"],
};

const commonRules = [
    {
        test: /\.css$/i,
        use: ['style-loader', 'css-loader']
    },
    {
        test: /\.(js|jsx|ts|tsx)$/,
        exclude: /node_modules/,
        use: {
            loader: "babel-loader",
            options: {
                presets: ["@babel/preset-env", "@babel/preset-react", "@babel/preset-typescript"]
            }
        }
    },
    {
        test: /\.(jpe?g|png|gif|svg)$/i,
        type: 'asset/resource',
        generator: {
            filename: "icons/[name][ext]"
        }
    },
];

module.exports = {
    commonOutput,
    commonResolve,
    commonRules,
};
"""
