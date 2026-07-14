import fs from 'fs';
import { shopCollections, turboCoinPacks } from './src/data/shop.ts';

fs.writeFileSync('shop_data.json', JSON.stringify(shopCollections, null, 2));
console.log('Shop data dumped to shop_data.json');
