import pluginVue from 'eslint-plugin-vue'
import pluginCypress from 'eslint-plugin-cypress'
import pluginVitest from '@vitest/eslint-plugin'
import pluginOxlint from 'eslint-plugin-oxlint'
import skipFormatting from 'eslint-config-prettier/flat'
import { defineConfigWithVueTs, vueTsConfigs } from '@vue/eslint-config-typescript'

// To allow more languages other than `ts` in `.vue` files, uncomment the following lines:
// import { configureVueProject } from '@vue/eslint-config-typescript'
// configureVueProject({ scriptLangs: ['ts', 'tsx'] })
// More info at https://github.com/vuejs/eslint-config-typescript/#advanced-setup


export default defineConfigWithVueTs(
  {
    name: 'app/files-to-lint',
    files: ['**/*.{vue,ts,mts,tsx}'],
    rules : {
      "vue/multi-word-component-names": ["error", {
        "ignores": ["Icon"]
      }]
    }
  },
  {
    ignores: ['**/dist/**', '**/dist-ssr/**', '**/node_modules/**', '**/env/**', '**/coverage/**', '**/djangospotifydownloader/**', "README.md"],
  },
  pluginVue.configs['flat/recommended'],
  vueTsConfigs.recommended,
  {
    ...pluginCypress.configs.recommended,
    files: [
      'cypress/e2e/**/*.{cy,spec}.{js,ts,jsx,tsx}',
      'cypress/support/**/*.{js,ts,jsx,tsx}',
    ],
  },
  {
    ...pluginVitest.configs.recommended,
    files: ['src/**/__tests__/*'],
  },

  ...pluginOxlint.buildFromOxlintConfigFile('.oxlintrc.json'),

  skipFormatting,
)

// export default defineConfigWithVueTs(
//   {
//     name: 'app/files-to-lint',
//     files: ['**/*.{vue,ts,mts,tsx}'],
//   },

//   {
//     ignores: ['**/dist/**', '**/dist-ssr/**', '**/coverage/**'],
//   },

//   // Vue Style Guide - Strongly Recommended rules
//   // Enforces: multi-word component names, PascalCase in templates, etc.
//   ...pluginVue.configs['flat/recommended'],

//   // Additional Vue Style Guide rules for component naming conventions
//   {
//     name: 'vue/style-guide-naming',
//     rules: {

//   },

//   vueTsConfigs.recommended,
//   {
//     ...pluginCypress.configs.recommended,
//     files: [
//       'cypress/e2e/**/*.{cy,spec}.{js,ts,jsx,tsx}',
//       'cypress/support/**/*.{js,ts,jsx,tsx}',
//     ],
//   },

//   {
//     ...pluginVitest.configs.recommended,
//     files: ['src/**/__tests__/*'],
//   },

//   ...pluginOxlint.buildFromOxlintConfigFile('.oxlintrc.json'),

//   skipFormatting,
// )
