#!/bin/bash

# Arrêter le script dès qu'une commande échoue
set -e

echo "Pre-build..."
echo ""
python scripts/pre_build.py
echo "--------------------------------"

echo "Make html..."
echo ""
make html
echo "--------------------------------"

echo "Linking _static directory..."
ln -sf _static/ _build/html/_static/
echo "--------------------------------"


echo "Post-build..."
echo ""
bash scripts/post_build.sh