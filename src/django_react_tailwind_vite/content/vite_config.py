VITE_CONFIG_CONTENT="""
import { defineConfig } from 'vite'
import tailwindcss from '@tailwindcss/vite'
import path from 'path'
import dotenv from 'dotenv'

// Load environment variables
dotenv.config({ path: './frontend/environments/.env.development' })

export default defineConfig({
  base: '/static/',
  plugins: [
    tailwindcss()
  ],
  resolve: {
    alias: {
      '@': path.resolve(__dirname, './frontend'),
      'images': path.resolve(__dirname, './frontend/src/images'),
    },
    extensions: ['.js', '.jsx', '.ts', '.tsx'],
  },
  build: {
    outDir: path.resolve(__dirname, './assets'),
    assetsDir: 'productionAssets',
    emptyOutDir: true, // Empty the output directory before build
    manifest: "manifest.json",
    rollupOptions: {
      input: {
        mainAssets: path.resolve(__dirname, './frontend/index.tsx'),
      },
    },
    sourcemap: true, // Generate source maps for development
  },
  define: {
    'process.env': JSON.stringify(process.env),
  },
})
"""