import io

import requests

from starkware.objects.availability import StateUpdate


async def is_valid(state_update: StateUpdate, batch_id: int) -> bool:
    """
    A hook for third parties to validate the state_update before signing the new root.
    """

    # Using io.environ instead of getenv to throw an error if the env var is not set
    url = io.environ['BATCH_VALIDATION_URL']

    # We only need vaults which contain balances for all vaults which are
    # affected by the batch.
    payload = { 'vaults': state_update.vaults, 'batchId': batch_id }
    response = requests.post(url, data = payload)

    if response.status_code == 200 or response.status_code == 204:
      return True

    return False
