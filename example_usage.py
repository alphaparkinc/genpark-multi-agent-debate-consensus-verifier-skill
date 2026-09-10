from client import MultiAgentDebateConsensusVerifierClient

def main():
    client = MultiAgentDebateConsensusVerifierClient()
    res = client.arbitrate_debate_consensus()
    print('Multi-Agent Debate Verifier: ' + res['consensus_id'] + ' (' + res['arbitrated_verdict'] + ')')
    print('Composite Confidence: ' + str(res['composite_confidence_score']) + ' | Hallucination: ' + res['hallucination_risk_level'])
    print('Consensus Dossier: ' + res['verified_consensus_dossier_url'])

if __name__ == '__main__':
    main()
