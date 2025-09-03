import type { ConfigType } from '@plone/registry';

export default function install(config: ConfigType) {
  config.settings.isMultilingual = false;
  config.settings.supportedLanguages = ['pt-br', 'pt-BR'];
  config.settings.defaultLanguage = 'pt-br';

  return config;
}
