# AWS ECS Scheduled Tasks Orb [![CircleCI status](https://circleci.com/gh/pbrisbin/aws-ecs-scheduled-tasks-orb.svg "CircleCI status")](https://circleci.com/gh/pbrisbin/aws-ecs-scheduled-tasks-orb)

Basically [aws-ecs](https://circleci.com/orbs/registry/orb/circleci/aws-ecs),
except updating a Schedule Task, instead of a Service.

## Usage

```yaml
version: 2.1

orbs:
  aws-ecs-scheduled-tasks: pbrisbin/aws-ecs-scheduled-tasks@x.y

workflows:
  commit:
    jobs:
      - aws-ecs-scheduled-tasks/deploy-scheduled-task-update:
          name: release
          family: my-app
          cluster-name: prod-services
          container-image-name-updates: 'container=api,tag=${CIRCLE_SHA1:0:10}'
```

---

[LICENSE](./LICENSE) | [CHANGELOG](./CHANGELOG.md)
