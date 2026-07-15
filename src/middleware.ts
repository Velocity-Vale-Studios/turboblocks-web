import { defineMiddleware } from "astro:middleware";

export const onRequest = defineMiddleware(async (context, next) => {
    const { url, cookies, redirect } = context;

    // Allow public assets and login page
    if (url.pathname.startsWith('/login') || url.pathname.startsWith('/_astro') || url.pathname.match(/\.(png|svg|ico|jpg|jpeg|webp)$/)) {
        return next();
    }

    const apiUrl = import.meta.env.PUBLIC_API_URL || 'http://localhost:8000';
    
    // Check maintenance mode
    try {
        const settingsRes = await fetch(`${apiUrl}/settings/maintenance_mode`);
        if (settingsRes.ok) {
            const data = await settingsRes.json();
            // If maintenance mode is NOT true, allow public access
            if (data.value !== "true") {
                return next();
            }
        }
    } catch (e) {
        console.error('Failed to fetch settings:', e);
        // Fail open or closed on backend unreachable?
        // For development, we fail closed (require auth), but if backend is down, auth also fails.
    }

    const token = cookies.get("auth_token")?.value;

    if (!token) {
        return redirect("/login");
    }

    // Validate the token by calling the backend
    try {
        const verifyRes = await fetch(`${apiUrl}/auth/me`, {
            headers: { 'Authorization': `Bearer ${token}` }
        });
        if (!verifyRes.ok) {
            cookies.delete('auth_token', { path: '/' });
            return redirect('/login');
        }
    } catch (e) {
        // If backend is unreachable, allow through (fail-open for development)
        // In production, this should fail-closed
        console.error('Token validation failed:', e);
    }

    return next();
});
