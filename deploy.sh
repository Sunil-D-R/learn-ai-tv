#!/bin/bash

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${BLUE}🔄 Starting site rebuild and deployment...${NC}"

# Step 1: Build the site
echo -e "${BLUE}🏗️ Building site with Hugo...${NC}"
hugo --minify
if [ $? -ne 0 ]; then
    echo -e "${RED}❌ Failed to build site${NC}"
    exit 1
fi

# Step 2: Deploy to GitHub
echo -e "${BLUE}🚀 Deploying to GitHub...${NC}"
cd public
git add .
git commit -m "auto: rebuild and deploy site $(date '+%Y-%m-%d %H:%M:%S')"
git push -f origin main

if [ $? -eq 0 ]; then
    echo -e "${GREEN}✅ Site successfully rebuilt and deployed!${NC}"
else
    echo -e "${RED}❌ Failed to deploy to GitHub${NC}"
    exit 1
fi
