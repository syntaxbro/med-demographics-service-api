#!/bin/bash

cp build/examples/resources/Patient.json build/examples/resources/Patient-Jayne-Smyth.json
cp build/examples/resources/Search_Patient.json build/examples/resources/Search_Patient-Jayne-Smyth.json
sed -i -e 's/9000000009/9000000010/g; s/Jane/Jayne/g; s/Smith/Smyth/g;' build/examples/resources/Patient-Jayne-Smyth.json
sed -i -e 's/9000000009/9000000010/g; s/Jane/Jayne/g; s/Smith/Smyth/g;' build/examples/resources/Search_Patient-Jayne-Smyth.json
sed -i -e 's/9000000009/9000000011/g; s/Jane/Janet/g; s/Smith/Smythe/g;'  build/examples/resources/Sensitive_Patient.json
sed -i -e 's/9000000009/9000000011/g; s/Jane/Janet/g; s/Smith/Smythe/g;'  build/examples/resources/Sensitive_Search_Patient.json
