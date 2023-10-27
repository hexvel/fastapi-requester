from models.bot import Bot


def search_model(*, base: str | None = None):
    if base == "bot":
        return Bot
