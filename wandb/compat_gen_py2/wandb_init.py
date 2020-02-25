# -*- coding: latin-1 -*-
"""
init.
"""

from prompt_toolkit import prompt
import wandb
from wandb.wandb_run import Run
from wandb.util.globals import set_global
# from wandb.internal.backend_grpc import Backend
from wandb.internal.backend_mp import Backend
import click
from wandb.stuff import util2

from wandb.apis import internal

# import typing
# if typing.TYPE_CHECKING:
#   from typing import Dict, List, Optional
#from typing import Optional, Dict

# priority order (highest to lowest):
# WANDB_FORCE_MODE
# settings.force_mode
# wandb.init(mode=)
# WANDB_MODE
# settings.mode
# ) -> Optional[Run]:


def init(settings = None,
         mode = None,
         entity=None,
         team=None,
         project=None,
         magic=None,
         config=None,
         reinit=None,
         name=None,
         group=None):
    """This is my comment.

    Intialize stuff.

    Args:
        settings: This is my setting.

    Returns:
        The return value
    """
    wl = wandb.setup()

    if mode == "noop":
        return None
    if mode == "test":
        return None

    api = internal.Api()
    if not api.api_key:
        key = prompt('Enter api key: ', is_password=True)
        util2.set_api_key(api, key)

    backend = Backend(mode=mode)
    backend.ensure_launched(log_fname=wl._log_internal_filename)
    backend.server_connect()

    # resuming needs access to the server, check server_status()?

    run = Run(config=config)
    run._set_backend(backend)

    settings = dict(entity="jeff", project="uncategorized")

    emojis = dict(star="⭐️", broom="🧹", rocket="🚀")
    url = "https://app.wandb.test/{}/{}/runs/{}".format(
        settings.get("entity"), settings.get("project"), run.run_id)
    wandb.termlog("{} View run at {}".format(
        emojis.get("rocket", ""), click.style(url, underline=True, fg='blue')))

    backend.run_update(dict(run_id=run.run_id, config=run.config._as_dict()))
    set_global(run=run, config=run.config, log=run.log, join=run.join)
    return run