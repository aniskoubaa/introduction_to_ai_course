#!/bin/bash

# update_repo.sh - Script to update the GitHub repository
# Repository: https://github.com/aniskoubaa/introduction_to_ai_course.git

set -e  # Exit on any error

echo "🚀 Starting repository update..."

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Check if we're in a git repository
if [ ! -d ".git" ]; then
    print_error "Not a git repository. Initializing..."
    git init
    git remote add origin https://github.com/aniskoubaa/introduction_to_ai_course.git
    print_success "Git repository initialized and remote added."
fi

# Check if remote origin exists
if ! git remote get-url origin &> /dev/null; then
    print_warning "Remote origin not found. Adding remote..."
    git remote add origin https://github.com/aniskoubaa/introduction_to_ai_course.git
    print_success "Remote origin added."
fi

# Get current branch name
current_branch=$(git rev-parse --abbrev-ref HEAD 2>/dev/null || echo "main")
print_status "Current branch: $current_branch"

# Check for uncommitted changes
if [ -n "$(git status --porcelain)" ]; then
    print_status "Uncommitted changes detected. Adding files..."
    
    # Show what will be added
    echo "Files to be added:"
    git status --porcelain
    
    # Add all changes
    git add .
    print_success "All changes added to staging area."
    
    # Get commit message from user or use default
    if [ -z "$1" ]; then
        commit_message="Update course materials - $(date '+%Y-%m-%d %H:%M:%S')"
        print_warning "No commit message provided. Using default: '$commit_message'"
    else
        commit_message="$1"
        print_status "Using commit message: '$commit_message'"
    fi
    
    # Commit changes
    git commit -m "$commit_message"
    print_success "Changes committed successfully."
else
    print_status "No uncommitted changes found."
fi

# Push to remote repository
print_status "Pushing to remote repository..."

# Check if the branch exists on remote
if git ls-remote --exit-code --heads origin $current_branch &> /dev/null; then
    # Branch exists, do a regular push
    git push origin $current_branch
else
    # Branch doesn't exist on remote, push with -u flag
    print_warning "Branch '$current_branch' doesn't exist on remote. Creating..."
    git push -u origin $current_branch
fi

print_success "Repository updated successfully!"
print_status "Repository URL: https://github.com/aniskoubaa/introduction_to_ai_course.git"

# Show current repository status
echo ""
print_status "Current repository status:"
git status --short
git log --oneline -5

echo ""
print_success "✅ Update complete! Your changes have been pushed to GitHub."
