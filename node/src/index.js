export function validateResearchAddress(value) {
  if (typeof value !== 'string' || value.trim().length === 0) throw new TypeError('address input required');
  return { accepted: true, purpose: 'public-or-synthetic-research', address: value.trim() };
}

export function prohibitedRecoveryOperation() {
  throw new Error('address-to-private-key recovery is outside the supported security boundary');
}
