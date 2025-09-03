import type { ConfigType } from '@plone/registry';
import installSettings from 'volto-plonegovbr-portal/config/settings';

function applyConfig(config: ConfigType) {
  installSettings(config);

  return config;
}

export default applyConfig;
