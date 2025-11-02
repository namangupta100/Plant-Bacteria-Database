# Quick Fix for Deployment Errors - UPDATED

## Issues Fixed (Version 2)

### 1. ✅ ALLOWED_HOSTS Error - ROBUST FIX
**Error:** `DisallowedHost: Invalid HTTP_HOST header: 'plant-bacteria-database-xcns.onrender.com'`

**Root Cause:** The `.onrender.com` wildcard wasn't being applied correctly in production.

**Solutions Applied:**
1. **Updated `build/settings.py`:**
   - Simplified ALLOWED_HOSTS logic
   - Automatically adds `.onrender.com` wildcard in production mode
   - Added explicit hostname support
   - In DEBUG mode, allows all hosts for local development

2. **Updated `render.yaml`:**
   - Set ALLOWED_HOSTS to: `plant-bacteria-database-xcns.onrender.com,.onrender.com`
   - This includes both your specific hostname AND the wildcard

### 2. ✅ Missing coreapi Package - GRACEFUL HANDLING
**Error:** `AssertionError: 'coreapi' must be installed for schema support.`

**Root Cause:** The `include_docs_urls` was being imported and called even when coreapi wasn't installed.

**Solution:**
- **Updated `pbd/urls.py`:**
  - Moved `include_docs_urls` import inside a try-except block
  - API docs will only be available if coreapi is successfully installed
  - App will work even if coreapi installation fails
  - Added to requirements.txt as well (belt-and-suspenders approach)

## Files Changed (Latest)

1. **requirements.txt** - Added REST framework dependencies (coreapi, coreschema, pyyaml)
2. **build/settings.py** - Robust ALLOWED_HOSTS handling with automatic wildcard support
3. **pbd/urls.py** - Graceful handling of missing coreapi package
4. **render.yaml** - Explicit hostname + wildcard for ALLOWED_HOSTS
5. **.env** - Updated for local development

## Immediate Action Required

### Step 1: Push Changes to GitHub

```bash
# Stage all changes
git add .

# Commit with descriptive message
git commit -m "Fix: Robust ALLOWED_HOSTS handling and graceful coreapi fallback"

# Push to trigger Render rebuild
git push
```

### Step 2: Verify Render Environment Variables

Go to your Render dashboard and ensure these are set:

| Variable | Value | Notes |
|----------|-------|-------|
| `SECRET_KEY` | (auto-generated) | Should be 50+ random chars |
| `DEBUG` | `False` | MUST be False in production |
| `DATABASE_URL` | (from PostgreSQL) | Auto-set from database |
| `ALLOWED_HOSTS` | `plant-bacteria-database-xcns.onrender.com,.onrender.com` | Include both! |
| `PYTHON_VERSION` | `3.10.0` | Or your preferred version |

### Step 3: Monitor Deployment

1. Watch the build logs in Render dashboard
2. Look for successful installation of coreapi
3. Verify migrations run successfully
4. Check that collectstatic completes

## What Changed in settings.py

```python
# OLD (problematic):
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '').split(',')

# NEW (robust):
ALLOWED_HOSTS = [host.strip() for host in allowed_hosts_str.split(',') if host.strip()]
if not DEBUG:
    # Always allow all Render.com subdomains in production
    if not any('.onrender.com' in h for h in ALLOWED_HOSTS):
        ALLOWED_HOSTS.append('.onrender.com')
    CSRF_TRUSTED_ORIGINS.append('https://*.onrender.com')
else:
    # Allow all hosts in DEBUG mode (local development)
    ALLOWED_HOSTS.append('*')
```

## What Changed in pbd/urls.py

```python
# OLD (problematic):
from rest_framework.documentation import include_docs_urls
urlpatterns = [
    ...
    path('api/docs/', include_docs_urls(...), name='schema-docs'),
]

# NEW (graceful):
try:
    from rest_framework.documentation import include_docs_urls
    urlpatterns.append(
        path('api/docs/', include_docs_urls(...), name='schema-docs')
    )
except (ImportError, AssertionError):
    pass  # coreapi not available, skip API docs
```

## Expected Result After Redeploy

- ✅ Homepage loads without errors at `https://plant-bacteria-database-xcns.onrender.com`
- ✅ No more ALLOWED_HOSTS errors
- ✅ If coreapi installs: API docs at `/api/docs/`
- ✅ If coreapi fails: App still works, just no docs endpoint
- ✅ All other pages functional
- ✅ Static files served correctly

## Troubleshooting

### If ALLOWED_HOSTS error persists:

**Option A: Set environment variable in Render manually**
1. Go to Render Dashboard → Your Service → Environment
2. Add or edit `ALLOWED_HOSTS`
3. Value: `plant-bacteria-database-xcns.onrender.com,.onrender.com,*` (temporary wildcard for testing)
4. Save and trigger manual deploy

**Option B: Check DEBUG mode**
```bash
# In Render Shell, verify:
python -c "import os; print('DEBUG:', os.environ.get('DEBUG')); print('ALLOWED_HOSTS:', os.environ.get('ALLOWED_HOSTS'))"
```

### If coreapi still fails:

This is now handled gracefully - the app will work, you just won't have `/api/docs/`. You can verify installation:

```bash
# In Render Shell:
pip list | grep coreapi
```

## Local Testing (Recommended)

Test these changes locally before pushing:

```powershell
# Activate venv
.\.venv\Scripts\Activate.ps1

# Install updated requirements
pip install -r requirements.txt

# Verify coreapi installed
pip show coreapi

# Run server
python manage.py runserver

# Test endpoints:
# http://127.0.0.1:8000/ (home)
# http://127.0.0.1:8000/api/docs/ (if coreapi works)
```

## Critical Notes

1. **ALLOWED_HOSTS now uses automatic wildcard** - The code automatically adds `.onrender.com` in production mode
2. **DEBUG must be False** - Verify in Render environment variables
3. **Graceful degradation** - App works even if coreapi fails to install
4. **Belt-and-suspenders** - Both explicit hostname AND wildcard are included

## Success Checklist

After deployment completes:

- [ ] Site loads at https://plant-bacteria-database-xcns.onrender.com
- [ ] No ALLOWED_HOSTS errors in logs
- [ ] Can navigate to different pages
- [ ] Static files (CSS/JS) load correctly
- [ ] Admin panel accessible at /admin
- [ ] API endpoints work at /api/bacteria/
- [ ] (Optional) API docs at /api/docs/ if coreapi installed
