from fastapi import APIRouter

router = APIRouter()


@router.get("/overview")
def overview() -> dict[str, list[str] | int]:
    return {
        "continue_watching": ["Interstellar", "Blade Runner 2049"],
        "recently_added": ["Dune: Part Two", "The Creator"],
        "stats": 42,
    }
