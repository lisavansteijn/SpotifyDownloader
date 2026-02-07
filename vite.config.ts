import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'

import vue from '@vitejs/plugin-vue'
import vueJsx from '@vitejs/plugin-vue-jsx'
import vueDevTools from 'vite-plugin-vue-devtools'
import Components from 'unplugin-vue-components/vite'

import tailwindcss from '@tailwindcss/vite'

// https://vite.dev/config/
export default defineConfig({
  plugins: [
    vue({
      // needed for pyscript
      template: {
        compilerOptions: {
          isCustomElement: (tag) => tag.includes("-"),
          whitespace: "preserve",
        },
      },
    }),
    vueJsx(),
    vueDevTools(),
    tailwindcss(),
    Components({
      dts: true,
      resolvers: [
        (componentName) => {
          // where `componentName` is always icon-solar-<icon-name>
          if (componentName.startsWith('icon-solar-'))
            return { name: componentName, from: 'solar' }
        },
      ],
    }),
  ],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    },
  },
})
