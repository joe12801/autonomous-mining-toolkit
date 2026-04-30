#!/bin/bash

# Autonomous Mining Toolkit - One-Click Installer for Hermes Agents
# Version: 1.0.0
# Author: Hermes Agent

set -e

RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}[1/4] Checking System Dependencies...${NC}"
commands=("git" "python3" "pip3" "gh")
for cmd in "${commands[@]}"; do
    if ! command -v $cmd &> /dev/null; then
        echo -e "${RED}Error: $cmd is not installed.${NC}"
        exit 1
    fi
done
echo -e "${GREEN}Dependencies OK.${NC}"

echo -e "${BLUE}[2/4] Setting up Python Environment...${NC}"
# Use current directory for absolute paths
INSTALL_DIR=$(pwd)
pip3 install -r requirements.txt --quiet
echo -e "${GREEN}Python requirements installed.${NC}"

echo -e "${BLUE}[3/4] Integrating with Hermes Agent Skills...${NC}"
# Determine Hermes profile path
HERMES_SKILL_PATH="$HOME/.hermes/profiles/default/skills/research/autonomous-research-mining"

# Support for custom profiles via environment variable
if [ ! -z "$HERMES_PROFILE" ]; then
    HERMES_SKILL_PATH="$HOME/.hermes/profiles/$HERMES_PROFILE/skills/research/autonomous-research-mining"
fi

mkdir -p "$HERMES_SKILL_PATH"

# Copy the SOP file as the primary SKILL.md
if [ -f "$INSTALL_DIR/SOP_Autonomous_Research_Mining_v2.md" ]; then
    cp "$INSTALL_DIR/SOP_Autonomous_Research_Mining_v2.md" "$HERMES_SKILL_PATH/SKILL.md"
    echo -e "${GREEN}SOP Skill imported to $HERMES_SKILL_PATH${NC}"
else
    echo -e "${RED}Warning: SOP file not found in $INSTALL_DIR${NC}"
fi

echo -e "${BLUE}[4/4] Verifying Installation...${NC}"
if [ -f "$INSTALL_DIR/driller.py" ]; then
    echo -e "${GREEN}Toolkit verified at $INSTALL_DIR${NC}"
else
    echo -e "${RED}Error: driller.py missing!${NC}"
    exit 1
fi

echo -e "\n${GREEN}===============================================${NC}"
echo -e "${GREEN}  Installation Complete! Ready for Mining.     ${NC}"
echo -e "${GREEN}===============================================${NC}"
echo -e "To start mining, tell your Agent:"
echo -e "  'Load skill autonomous-research-mining and mine [URL]'"
echo -e "${GREEN}===============================================${NC}"
