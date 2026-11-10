# Release a new version 
git add .
git commit -m "Release v0.0.1"
git push origin main
git tag v0.0.1
git push origin v0.0.1
gh release create v0.0.1 --title "v0.0.1" --notes "First release"


# Delete an old version 
gh release delete v0.0.1 --yes
git push origin --delete v0.0.1
git tag -d v0.0.1
git add .
git commit -m "Release v0.0.1"
git push origin main
git tag v0.0.1
git push origin v0.0.1
gh release create v0.0.1 --title "v0.0.1" --notes "First release"

