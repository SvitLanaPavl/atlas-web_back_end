-- Old school band
-- Lists all bands with Glam rock as their main style
SELECT band_name,
COALESCE(split, YEAR(CURRENT_DATE)) - formed AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC;