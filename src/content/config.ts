import { defineCollection, z } from 'astro:content';

const blogCollection = defineCollection({
    type: 'content',
    schema: z.object({
        title: z.string(),
        date: z.string(),
        tag: z.string(),
        featured: z.boolean().default(false),
        icon: z.string(),
        desc: z.string(),
        gradient: z.string(),
        borderColorClass: z.string(),
        glowClass: z.string(),
        accent: z.string(),
        btnHoverAccent: z.string(),
        textHoverAccent: z.string(),
        shadowAccent: z.string(),
        borderAccent: z.string(),
        bgAccent: z.string(),
    }),
});

export const collections = {
    'blog': blogCollection,
};