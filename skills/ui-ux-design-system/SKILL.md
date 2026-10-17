---
name: ui-ux-design-system
description: UI/UX design standards and anti-generic visual principles. Enforces design tokens, WCAG 2.2 accessibility, 5-state component matrices, and distinctive visual character.
---

# UI/UX Design System & Anti-Generic Standards

## 1. Anti-Generic Principles (Combatting AI Slop)
Reject generic, template-driven AI aesthetics:
- ❌ Do NOT use unmotivated neon purple/blue gradient backgrounds.
- ❌ Do NOT use generic floating card grids without functional grouping.
- ❌ Do NOT use heavy glassmorphism that degrades text contrast.
- ❌ Do NOT use lorem ipsum; write contextual, production-ready copy.
- ✅ Define semantic color tokens with functional meaning (primary, neutral, success, warning, danger).
- ✅ Establish high visual contrast and an unmistakable primary Call-to-Action (CTA).

## 2. Accessibility Guidelines (WCAG 2.2 AA)
- Contrast ratio between text and background must be at least 4.5:1 for standard text (3:1 for large text).
- Interactive touch targets on mobile viewports must measure at least 44x44px.
- Visible focus rings must be implemented for all keyboard navigation states.

## 3. Mandatory 5-State Matrix
Every view and component specification must explicitly define 5 states:
1. **Default:** Standard presentation when data is loaded.
2. **Loading:** Proportionate skeleton/shimmer placeholder.
3. **Empty:** Contextual illustration and actionable empty-state CTA.
4. **Error:** Clear human-readable explanation with a retry trigger.
5. **Success:** Positive visual confirmation of completed user action.
