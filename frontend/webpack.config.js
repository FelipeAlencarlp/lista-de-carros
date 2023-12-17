const webpack = require('webpack');

export const resolve = {
    fallback: {
        crypto: require.resolve('crypto-browserify'),
        stream: require.resolve('stream-browserify'),
        buffer: require.resolve('buffer'),
        process: require.resolve('process/browser'),
    },
    plugins: [
        new webpack.ProvidePlugin({
          process: 'process/browser',
        }),
      ],
};